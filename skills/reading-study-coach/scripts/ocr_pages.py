#!/usr/bin/env python3
"""Run page-level OCR for scanned PDFs when local OCR tools are available.

This script intentionally does not install OCR tools. It detects and uses:

- pdftoppm: renders PDF pages to images.
- tesseract: performs OCR on rendered page images.

Outputs:
- ocr_report.json
- ocr_report.md
- ocr_pages.jsonl
- ocr_text/page-001.txt, page-002.txt, ...

If the tools are missing, the script writes a diagnostic report and exits with
code 3 so the reading workflow can clearly say OCR is needed but unavailable.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


@dataclass
class OCRPageRecord:
    page: int
    status: str
    char_count: int
    text_path: str | None
    image_path: str | None
    error: str | None


def which(name: str) -> str | None:
    return shutil.which(name)


def detect_tools() -> dict[str, str | None]:
    return {
        "pdftoppm": which("pdftoppm"),
        "tesseract": which("tesseract"),
    }


def get_page_count(pdf_path: Path) -> int | None:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        try:
            from PyPDF2 import PdfReader  # type: ignore
        except Exception:
            return None

    try:
        return len(PdfReader(str(pdf_path)).pages)
    except Exception:
        return None


def run_command(command: list[str], timeout: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def render_page(
    pdf_path: Path,
    page: int,
    image_dir: Path,
    dpi: int,
    timeout: int,
) -> tuple[Path | None, str | None]:
    prefix = image_dir / f"page-{page:03d}"
    command = [
        "pdftoppm",
        "-r",
        str(dpi),
        "-f",
        str(page),
        "-l",
        str(page),
        "-png",
        str(pdf_path),
        str(prefix),
    ]
    result = run_command(command, timeout)
    if result.returncode != 0:
        return None, result.stderr.strip() or result.stdout.strip() or "pdftoppm failed"

    candidates = sorted(image_dir.glob(f"page-{page:03d}*.png"))
    if not candidates:
        return None, "pdftoppm produced no image"
    return candidates[0], None


def ocr_image(image_path: Path, lang: str, psm: str, timeout: int) -> tuple[str, str | None]:
    command = ["tesseract", str(image_path), "stdout", "-l", lang, "--psm", psm]
    result = run_command(command, timeout)
    if result.returncode != 0:
        return "", result.stderr.strip() or result.stdout.strip() or "tesseract failed"
    return result.stdout.strip(), None


def write_report(
    report: dict,
    records: list[OCRPageRecord],
    out_dir: Path,
) -> None:
    (out_dir / "ocr_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    with (out_dir / "ocr_pages.jsonl").open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")

    lines = [
        "# OCR Report",
        "",
        f"- Input: `{report['input']}`",
        f"- Generated at: {report['generated_at']}",
        f"- Status: {report['status']}",
        f"- Pages requested: {report['pages_requested']}",
        f"- Pages completed: {report['pages_completed']}",
        f"- Language: {report['language']}",
        f"- DPI: {report['dpi']}",
        "",
        "## Tools",
        "",
    ]
    for name, path in report["tools"].items():
        lines.append(f"- {name}: {path or 'not found'}")

    if report.get("message"):
        lines.extend(["", "## Message", "", report["message"]])

    lines.extend(["", "## Page Results", ""])
    lines.append("| Page | Status | Characters | Text Path | Error |")
    lines.append("|---|---|---:|---|---|")
    for record in records:
        lines.append(
            f"| {record.page} | {record.status} | {record.char_count} | "
            f"{record.text_path or ''} | {record.error or ''} |"
        )

    (out_dir / "ocr_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run page-level OCR for a PDF.")
    parser.add_argument("pdf", help="Path to the PDF file.")
    parser.add_argument("--out", default="ocr-output", help="Output directory.")
    parser.add_argument("--lang", default="eng+chi_sim", help="Tesseract language list.")
    parser.add_argument("--dpi", type=int, default=220, help="Render DPI for OCR images.")
    parser.add_argument("--first-page", type=int, default=1, help="First 1-based page.")
    parser.add_argument("--last-page", type=int, default=None, help="Last 1-based page.")
    parser.add_argument("--psm", default="6", help="Tesseract page segmentation mode.")
    parser.add_argument("--timeout", type=int, default=120, help="Per-command timeout seconds.")
    parser.add_argument("--keep-images", action="store_true", help="Keep rendered page PNGs.")
    parser.add_argument("--diagnose-only", action="store_true", help="Only check OCR tools.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    tools = detect_tools()
    page_count = get_page_count(pdf_path)
    last_page = args.last_page or page_count or args.first_page
    pages = list(range(args.first_page, last_page + 1))
    records: list[OCRPageRecord] = []

    base_report = {
        "input": str(pdf_path),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "not_started",
        "message": "",
        "tools": tools,
        "page_count": page_count,
        "pages_requested": pages,
        "pages_completed": 0,
        "language": args.lang,
        "dpi": args.dpi,
    }

    if not pdf_path.exists() or pdf_path.suffix.lower() != ".pdf":
        base_report["status"] = "failed"
        base_report["message"] = "Input file was not found or is not a PDF."
        write_report(base_report, records, out_dir)
        print(out_dir / "ocr_report.md")
        return 2

    missing = [name for name, path in tools.items() if not path]
    if missing:
        base_report["status"] = "tools_missing"
        base_report["message"] = (
            "OCR cannot run because required tools are missing: "
            + ", ".join(missing)
            + ". Install Poppler/pdftoppm and Tesseract, or provide OCR text/page images."
        )
        write_report(base_report, records, out_dir)
        print(out_dir / "ocr_report.md")
        return 3

    if args.diagnose_only:
        base_report["status"] = "ready"
        base_report["message"] = "OCR tools are available."
        write_report(base_report, records, out_dir)
        print(out_dir / "ocr_report.md")
        return 0

    text_dir = out_dir / "ocr_text"
    text_dir.mkdir(parents=True, exist_ok=True)
    image_out_dir = out_dir / "ocr_images"

    with tempfile.TemporaryDirectory() as temp_dir_name:
        image_dir = image_out_dir if args.keep_images else Path(temp_dir_name)
        image_dir.mkdir(parents=True, exist_ok=True)

        for page in pages:
            image_path, render_error = render_page(
                pdf_path,
                page,
                image_dir,
                args.dpi,
                args.timeout,
            )
            if render_error or image_path is None:
                records.append(
                    OCRPageRecord(
                        page=page,
                        status="render_failed",
                        char_count=0,
                        text_path=None,
                        image_path=None,
                        error=render_error,
                    )
                )
                continue

            text, ocr_error = ocr_image(image_path, args.lang, args.psm, args.timeout)
            if ocr_error:
                records.append(
                    OCRPageRecord(
                        page=page,
                        status="ocr_failed",
                        char_count=0,
                        text_path=None,
                        image_path=str(image_path.relative_to(out_dir))
                        if args.keep_images
                        else None,
                        error=ocr_error,
                    )
                )
                continue

            text_path = text_dir / f"page-{page:03d}.txt"
            text_path.write_text(text + "\n", encoding="utf-8")
            records.append(
                OCRPageRecord(
                    page=page,
                    status="ok",
                    char_count=len(text),
                    text_path=str(text_path.relative_to(out_dir)),
                    image_path=str(image_path.relative_to(out_dir)) if args.keep_images else None,
                    error=None,
                )
            )

    completed = sum(1 for record in records if record.status == "ok")
    base_report["status"] = "completed" if completed == len(pages) else "partial"
    base_report["pages_completed"] = completed
    if completed == 0:
        base_report["message"] = "No pages were successfully OCRed."
    elif completed < len(pages):
        base_report["message"] = "Some pages failed OCR. Inspect the page results."
    else:
        base_report["message"] = "OCR completed. Use ocr_pages.jsonl and ocr_text/ for reading."

    write_report(base_report, records, out_dir)
    print(out_dir / "ocr_report.md")
    return 0 if completed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
