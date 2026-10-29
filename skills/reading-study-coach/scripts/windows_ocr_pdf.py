#!/usr/bin/env python3
"""OCR scanned PDFs with Windows built-in OCR.

This path avoids Poppler/pdftoppm and Tesseract when the PDF already contains
page images that pypdf can extract. It is intended for Windows Codex sessions.

Outputs:
- windows_ocr_report.json
- windows_ocr_report.md
- ocr_pages.jsonl
- ocr_text/page-001.txt, ...
- page_images/page-001-image-01.png, ... when --keep-images is used
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


@dataclass
class PageOCRRecord:
    page: int
    status: str
    image_count: int
    images_ocr_done: int
    char_count: int
    text_path: str | None
    image_paths: list[str]
    errors: list[str]


def import_pdf_reader():
    try:
        from pypdf import PdfReader  # type: ignore

        return PdfReader
    except Exception as exc:
        raise RuntimeError("pypdf is required for Windows OCR image extraction.") from exc


def import_pillow():
    try:
        from PIL import Image  # type: ignore

        return Image
    except Exception as exc:
        raise RuntimeError("Pillow is required to normalize extracted PDF images.") from exc


def powershell_executable() -> str | None:
    return shutil.which("powershell.exe") or shutil.which("powershell") or shutil.which("pwsh")


def clean_ocr_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"(?<=[\u3400-\u4dbf\u4e00-\u9fff])\s+(?=[\u3400-\u4dbf\u4e00-\u9fff])", "", text)
    text = re.sub(r"\s+([，。！？；：、）》】])", r"\1", text)
    text = re.sub(r"([《（【])\s+", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def resize_if_needed(image, max_side: int):
    if max_side <= 0:
        return image
    width, height = image.size
    largest = max(width, height)
    if largest <= max_side:
        return image
    scale = max_side / largest
    new_size = (max(1, int(width * scale)), max(1, int(height * scale)))
    return image.resize(new_size)


def save_pdf_image(image_obj, output_path: Path, max_side: int) -> tuple[bool, str | None]:
    Image = import_pillow()
    try:
        image = getattr(image_obj, "image", None)
        if image is None:
            from io import BytesIO

            image = Image.open(BytesIO(image_obj.data))
        image = resize_if_needed(image, max_side)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(output_path, format="PNG")
        return True, None
    except Exception as exc:
        return False, str(exc)


def run_windows_ocr(ps_script: Path, image_path: Path, language: str, timeout: int) -> tuple[str, str | None]:
    ps = powershell_executable()
    if not ps:
        return "", "PowerShell executable not found."

    command = [
        ps,
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(ps_script),
        "-ImagePath",
        str(image_path),
        "-Language",
        language,
    ]
    result = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    if result.returncode != 0:
        return "", result.stderr.strip() or result.stdout.strip() or "Windows OCR failed."
    return clean_ocr_text(result.stdout), None


def write_outputs(report: dict, records: list[PageOCRRecord], out_dir: Path) -> None:
    (out_dir / "windows_ocr_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    with (out_dir / "ocr_pages.jsonl").open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")

    lines = [
        "# Windows OCR Report",
        "",
        f"- Input: `{report['input']}`",
        f"- Generated at: {report['generated_at']}",
        f"- Status: {report['status']}",
        f"- Pages requested: {report['pages_requested']}",
        f"- Pages completed: {report['pages_completed']}",
        f"- Language: {report['language']}",
        f"- PowerShell: {report['powershell'] or 'not found'}",
        f"- Helper script: `{report['helper_script']}`",
        f"- Keep images: {report['keep_images']}",
        "",
        "## Message",
        "",
        report["message"],
        "",
        "## Page Results",
        "",
        "| Page | Status | Images | OCR Done | Characters | Text Path | Errors |",
        "|---|---|---:|---:|---:|---|---|",
    ]
    for record in records:
        errors = "; ".join(record.errors)
        lines.append(
            f"| {record.page} | {record.status} | {record.image_count} | "
            f"{record.images_ocr_done} | {record.char_count} | "
            f"{record.text_path or ''} | {errors} |"
        )
    (out_dir / "windows_ocr_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OCR a scanned PDF with Windows built-in OCR.")
    parser.add_argument("pdf", help="Path to the PDF file.")
    parser.add_argument("--out", default="windows-ocr-output", help="Output directory.")
    parser.add_argument("--lang", default="zh-Hans-CN", help="Windows OCR language tag.")
    parser.add_argument("--first-page", type=int, default=1, help="First 1-based page.")
    parser.add_argument("--last-page", type=int, default=None, help="Last 1-based page.")
    parser.add_argument("--timeout", type=int, default=120, help="Per-image OCR timeout seconds.")
    parser.add_argument("--keep-images", action="store_true", help="Keep normalized page images.")
    parser.add_argument(
        "--max-side",
        type=int,
        default=2600,
        help="Downscale extracted images so the longest side is at most this many pixels. Use 0 to disable.",
    )
    parser.add_argument("--diagnose-only", action="store_true", help="Only check Windows OCR prerequisites.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    ps_script = Path(__file__).with_name("windows_ocr_image.ps1").resolve()
    ps = powershell_executable()

    base_report = {
        "input": str(pdf_path),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "not_started",
        "message": "",
        "pages_requested": [],
        "pages_completed": 0,
        "language": args.lang,
        "powershell": ps,
        "helper_script": str(ps_script),
        "keep_images": bool(args.keep_images),
        "max_side": args.max_side,
    }
    records: list[PageOCRRecord] = []

    if not pdf_path.exists() or pdf_path.suffix.lower() != ".pdf":
        base_report["status"] = "failed"
        base_report["message"] = "Input file was not found or is not a PDF."
        write_outputs(base_report, records, out_dir)
        print(out_dir / "windows_ocr_report.md")
        return 2

    if not ps:
        base_report["status"] = "tools_missing"
        base_report["message"] = "PowerShell is required for Windows OCR but was not found."
        write_outputs(base_report, records, out_dir)
        print(out_dir / "windows_ocr_report.md")
        return 3

    if not ps_script.exists():
        base_report["status"] = "failed"
        base_report["message"] = f"Windows OCR helper script not found: {ps_script}"
        write_outputs(base_report, records, out_dir)
        print(out_dir / "windows_ocr_report.md")
        return 2

    try:
        PdfReader = import_pdf_reader()
        import_pillow()
        reader = PdfReader(str(pdf_path))
    except Exception as exc:
        base_report["status"] = "failed"
        base_report["message"] = str(exc)
        write_outputs(base_report, records, out_dir)
        print(out_dir / "windows_ocr_report.md")
        return 1

    page_count = len(reader.pages)
    last_page = args.last_page or page_count
    pages = list(range(args.first_page, min(last_page, page_count) + 1))
    base_report["pages_requested"] = pages

    if args.diagnose_only:
        base_report["status"] = "ready"
        base_report["message"] = "Windows OCR prerequisites are available. Run without --diagnose-only to OCR pages."
        write_outputs(base_report, records, out_dir)
        print(out_dir / "windows_ocr_report.md")
        return 0

    text_dir = out_dir / "ocr_text"
    text_dir.mkdir(parents=True, exist_ok=True)
    kept_images_dir = out_dir / "page_images"

    with tempfile.TemporaryDirectory() as temp_dir_name:
        image_root = kept_images_dir if args.keep_images else Path(temp_dir_name)
        image_root.mkdir(parents=True, exist_ok=True)

        for page_no in pages:
            page = reader.pages[page_no - 1]
            image_objects = list(getattr(page, "images", []))
            errors: list[str] = []
            image_paths: list[str] = []
            page_texts: list[str] = []
            images_done = 0

            for image_index, image_obj in enumerate(image_objects, start=1):
                image_path = image_root / f"page-{page_no:03d}-image-{image_index:02d}.png"
                saved, save_error = save_pdf_image(image_obj, image_path, args.max_side)
                if not saved:
                    errors.append(f"image {image_index}: save failed: {save_error}")
                    continue

                if args.keep_images:
                    image_paths.append(str(image_path.relative_to(out_dir)))

                text, ocr_error = run_windows_ocr(ps_script, image_path, args.lang, args.timeout)
                if ocr_error:
                    errors.append(f"image {image_index}: {ocr_error}")
                    continue
                images_done += 1
                if text:
                    page_texts.append(text)

            combined = clean_ocr_text("\n\n".join(page_texts))
            text_path: str | None = None
            if combined:
                target = text_dir / f"page-{page_no:03d}.txt"
                target.write_text(combined + "\n", encoding="utf-8")
                text_path = str(target.relative_to(out_dir))

            if combined and images_done:
                status = "ok"
            elif images_done:
                status = "empty_ocr"
            elif image_objects:
                status = "ocr_failed"
            else:
                status = "no_images"

            records.append(
                PageOCRRecord(
                    page=page_no,
                    status=status,
                    image_count=len(image_objects),
                    images_ocr_done=images_done,
                    char_count=len(combined),
                    text_path=text_path,
                    image_paths=image_paths,
                    errors=errors,
                )
            )

    completed = sum(1 for record in records if record.status == "ok")
    base_report["pages_completed"] = completed
    if completed == len(records) and records:
        base_report["status"] = "completed"
        base_report["message"] = "Windows OCR completed for all requested pages."
    elif completed:
        base_report["status"] = "partial"
        base_report["message"] = "Windows OCR completed for some pages. Inspect failed or empty pages."
    else:
        base_report["status"] = "failed"
        base_report["message"] = "Windows OCR did not produce text for any requested page."

    write_outputs(base_report, records, out_dir)
    print(out_dir / "windows_ocr_report.md")
    return 0 if completed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
