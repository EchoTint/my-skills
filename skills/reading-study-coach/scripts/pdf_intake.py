#!/usr/bin/env python3
"""Diagnose PDF readability and extract page-level text.

Outputs:
- intake_report.json
- intake_report.md
- pages.jsonl
- pages/page-001.txt, page-002.txt, ...

This script intentionally does not pretend to OCR by default. It detects when
OCR or page-image reading is likely needed and reports that clearly.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import statistics
import sys
import unicodedata


@dataclass
class PageRecord:
    page: int
    char_count: int
    line_count: int
    nonempty_line_count: int
    suspicious_char_ratio: float
    table_like: bool
    quality: str
    needs_review: bool
    extraction_error: str | None
    text_path: str | None


def import_pdf_reader():
    try:
        from pypdf import PdfReader  # type: ignore

        return PdfReader, "pypdf"
    except Exception:
        pass

    try:
        from PyPDF2 import PdfReader  # type: ignore

        return PdfReader, "PyPDF2"
    except Exception as exc:
        raise RuntimeError(
            "No PDF reader found. Install pypdf or PyPDF2, then rerun."
        ) from exc


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text.strip()


def suspicious_char_ratio(text: str) -> float:
    if not text:
        return 0.0

    suspicious = 0
    for ch in text:
        category = unicodedata.category(ch)
        if ch == "\ufffd":
            suspicious += 1
        elif category.startswith("C") and ch not in "\n\t ":
            suspicious += 1
        elif 0xE000 <= ord(ch) <= 0xF8FF:
            suspicious += 1
    return suspicious / max(1, len(text))


def looks_table_like(lines: list[str]) -> bool:
    candidates = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if "\t" in stripped or "|" in stripped:
            candidates += 1
        elif len(re.findall(r"\s{2,}", stripped)) >= 2:
            candidates += 1
    return candidates >= 3


def classify_page(char_count: int, suspicious_ratio: float, error: str | None) -> str:
    if error:
        return "error"
    if char_count == 0:
        return "empty"
    if suspicious_ratio >= 0.08:
        return "low"
    if char_count < 100:
        return "low"
    if char_count < 500:
        return "medium"
    return "high"


def sample_pages(page_count: int, max_samples: int) -> list[int]:
    if page_count <= 0:
        return []
    wanted = {1, 2, 3, page_count, max(1, page_count - 1)}
    wanted.add(max(1, page_count // 2))
    wanted.add(max(1, page_count // 3))
    wanted.add(max(1, (page_count * 2) // 3))
    for n in range(1, min(page_count, 10) + 1):
        wanted.add(n)
    ordered = sorted(n for n in wanted if 1 <= n <= page_count)
    if len(ordered) <= max_samples:
        return ordered
    if max_samples <= 1:
        return [1]
    step = (len(ordered) - 1) / (max_samples - 1)
    return [ordered[round(i * step)] for i in range(max_samples)]


def detect_toc(text_by_page: list[str], outline_present: bool) -> bool:
    if outline_present:
        return True
    sample = "\n".join(text_by_page[: min(12, len(text_by_page))]).lower()
    markers = ["table of contents", "contents", "目录", "目錄"]
    return any(marker in sample for marker in markers)


def classify_document(records: list[PageRecord]) -> tuple[str, str, str]:
    if not records:
        return "unknown", "low", "ocr_or_page_images"

    total = len(records)
    meaningful = sum(1 for r in records if r.char_count >= 100 and not r.extraction_error)
    high = sum(1 for r in records if r.quality == "high")
    empty_or_low = sum(1 for r in records if r.quality in {"empty", "low", "error"})
    suspicious = statistics.mean(r.suspicious_char_ratio for r in records)
    coverage = meaningful / total
    high_ratio = high / total
    low_ratio = empty_or_low / total

    if coverage < 0.10:
        return "scanned_or_image_based", "low", "ocr_or_page_images"
    if coverage < 0.65 or low_ratio > 0.35:
        return "mixed", "medium", "text_plus_ocr_or_visual_checks"
    if suspicious >= 0.05:
        return "text_based_but_suspicious", "medium", "text_plus_spot_checks"
    if high_ratio >= 0.70:
        return "text_based", "high", "text_extraction"
    return "layout_complex_or_short_text", "medium", "text_plus_spot_checks"


def read_pdf(pdf_path: Path, out_dir: Path, max_page_chars: int) -> dict:
    PdfReader, reader_name = import_pdf_reader()
    reader = PdfReader(str(pdf_path))
    pages_dir = out_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    outline_present = False
    try:
        outline_present = bool(getattr(reader, "outline", None))
    except Exception:
        outline_present = False

    records: list[PageRecord] = []
    text_by_page: list[str] = []

    for index, page in enumerate(reader.pages, start=1):
        error: str | None = None
        try:
            text = page.extract_text() or ""
        except Exception as exc:  # pragma: no cover - depends on PDF parser
            text = ""
            error = str(exc)
        text = normalize_text(text)
        text_by_page.append(text)
        lines = text.splitlines()
        nonempty_lines = [line for line in lines if line.strip()]
        suspicious = suspicious_char_ratio(text)
        quality = classify_page(len(text), suspicious, error)
        needs_review = quality in {"empty", "low", "error"} or suspicious >= 0.05
        text_path: str | None = None
        if text:
            page_path = pages_dir / f"page-{index:03d}.txt"
            page_path.write_text(text[:max_page_chars], encoding="utf-8")
            text_path = str(page_path.relative_to(out_dir))

        records.append(
            PageRecord(
                page=index,
                char_count=len(text),
                line_count=len(lines),
                nonempty_line_count=len(nonempty_lines),
                suspicious_char_ratio=round(suspicious, 4),
                table_like=looks_table_like(nonempty_lines),
                quality=quality,
                needs_review=needs_review,
                extraction_error=error,
                text_path=text_path,
            )
        )

    pdf_type, text_quality, recommended_mode = classify_document(records)
    toc_detected = detect_toc(text_by_page, outline_present)
    sample = sample_pages(len(records), max_samples=12)
    review_pages = [
        r.page
        for r in records
        if r.needs_review or r.table_like
    ][:50]

    report = {
        "input": str(pdf_path),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "reader": reader_name,
        "pages": len(records),
        "pdf_type": pdf_type,
        "text_extraction_quality": text_quality,
        "recommended_mode": recommended_mode,
        "toc_detected": toc_detected,
        "outline_detected": outline_present,
        "ocr_requested": False,
        "ocr_engine_detected": bool(shutil.which("tesseract")),
        "sample_pages": sample,
        "pages_needing_review": review_pages,
        "metrics": {
            "empty_page_ratio": round(
                sum(1 for r in records if r.quality == "empty") / max(1, len(records)), 4
            ),
            "low_quality_page_ratio": round(
                sum(1 for r in records if r.quality in {"empty", "low", "error"})
                / max(1, len(records)),
                4,
            ),
            "high_quality_page_ratio": round(
                sum(1 for r in records if r.quality == "high") / max(1, len(records)), 4
            ),
            "average_chars_per_page": round(
                statistics.mean([r.char_count for r in records]) if records else 0, 1
            ),
            "median_chars_per_page": round(
                statistics.median([r.char_count for r in records]) if records else 0, 1
            ),
            "average_suspicious_char_ratio": round(
                statistics.mean([r.suspicious_char_ratio for r in records])
                if records
                else 0,
                4,
            ),
            "table_like_pages": [r.page for r in records if r.table_like][:50],
        },
        "pages_detail": [asdict(r) for r in records],
    }
    return report


def write_jsonl(report: dict, out_dir: Path) -> None:
    path = out_dir / "pages.jsonl"
    with path.open("w", encoding="utf-8") as handle:
        for record in report["pages_detail"]:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_report_json(report: dict, out_dir: Path) -> None:
    (out_dir / "intake_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_report_md(report: dict, out_dir: Path) -> None:
    lines = [
        "# PDF Intake Report",
        "",
        f"- Input: `{report['input']}`",
        f"- Pages: {report['pages']}",
        f"- PDF type: {report['pdf_type']}",
        f"- Text extraction quality: {report['text_extraction_quality']}",
        f"- Recommended mode: {report['recommended_mode']}",
        f"- Table of contents detected: {'yes' if report['toc_detected'] else 'no'}",
        f"- Outline/bookmarks detected: {'yes' if report['outline_detected'] else 'no'}",
        f"- OCR engine detected: {'yes' if report['ocr_engine_detected'] else 'no'}",
        "",
        "## Metrics",
        "",
    ]
    for key, value in report["metrics"].items():
        lines.append(f"- {key}: {value}")

    lines.extend(
        [
            "",
            "## Sample Pages",
            "",
            ", ".join(str(page) for page in report["sample_pages"]) or "None",
            "",
            "## Pages Needing Review",
            "",
            ", ".join(str(page) for page in report["pages_needing_review"])
            or "None",
            "",
            "## Recommendation",
            "",
        ]
    )

    mode = report["recommended_mode"]
    if mode == "text_extraction":
        lines.append(
            "Proceed with extracted text, preserving page references. Spot-check visual pages if diagrams or tables matter."
        )
    elif mode == "text_plus_spot_checks":
        lines.append(
            "Use extracted text, but spot-check sampled pages and important visual/table pages before deep analysis."
        )
    elif mode == "text_plus_ocr_or_visual_checks":
        lines.append(
            "Combine extracted text with OCR or page-image inspection for weak pages. Do not treat the extraction as complete."
        )
        lines.append(
            "On Windows, first try: `python scripts/windows_ocr_pdf.py <pdf> --out <windows-ocr-output> --lang zh-Hans-CN`."
        )
        lines.append(
            "For AI vision OCR preparation, run: `python scripts/prepare_vision_ocr.py <pdf> --out <vision-ocr-input>`."
        )
        lines.append(
            "Use Tesseract fallback only when Poppler/pdftoppm and Tesseract are installed: `python scripts/ocr_pages.py <pdf> --out <ocr-output>`."
        )
    else:
        lines.append(
            "Use OCR or page-image reading before analysis. Plain text extraction is not reliable enough."
        )
        lines.append(
            "On Windows, first try: `python scripts/windows_ocr_pdf.py <pdf> --out <windows-ocr-output> --lang zh-Hans-CN`."
        )
        lines.append(
            "For AI vision OCR preparation, run: `python scripts/prepare_vision_ocr.py <pdf> --out <vision-ocr-input>`."
        )
        lines.append(
            "Use Tesseract fallback only when Poppler/pdftoppm and Tesseract are installed: `python scripts/ocr_pages.py <pdf> --out <ocr-output>`."
        )

    lines.extend(
        [
            "",
            "## Evidence Policy",
            "",
            "For scanned, mixed, or low-quality PDFs, separate reading claims into confirmed evidence, reasoned inference, and items needing OCR/rereading.",
            "Do not let missing OCR become a shallow outline, but do not present inferred chapter functions as fully confirmed either.",
        ]
    )

    (out_dir / "intake_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Diagnose PDF readability.")
    parser.add_argument("pdf", help="Path to the PDF file.")
    parser.add_argument("--out", default="pdf-intake-output", help="Output directory.")
    parser.add_argument(
        "--max-page-chars",
        type=int,
        default=12000,
        help="Maximum characters to save per page text file.",
    )
    parser.add_argument(
        "--ocr",
        choices=["none", "auto", "force"],
        default="none",
        help="Reserved OCR mode. This version reports OCR need but does not run OCR.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    pdf_path = Path(args.pdf).expanduser().resolve()
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 2
    if pdf_path.suffix.lower() != ".pdf":
        print(f"Input does not look like a PDF: {pdf_path}", file=sys.stderr)
        return 2

    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        report = read_pdf(pdf_path, out_dir, args.max_page_chars)
    except Exception as exc:
        print(f"PDF intake failed: {exc}", file=sys.stderr)
        return 1

    report["ocr_requested"] = args.ocr != "none"
    if args.ocr != "none":
        report["ocr_note"] = (
            "OCR execution is not implemented in this lightweight script. "
            "Use scripts/windows_ocr_pdf.py, scripts/prepare_vision_ocr.py, "
            "scripts/ocr_pages.py, or another OCR-capable tool if recommended_mode requires it."
        )

    write_report_json(report, out_dir)
    write_jsonl(report, out_dir)
    write_report_md(report, out_dir)
    print(out_dir / "intake_report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
