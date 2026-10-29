#!/usr/bin/env python3
"""Prepare PDF page images for AI vision OCR.

This does not call any API. It extracts embedded PDF images, normalizes them to
PNG, writes a manifest, and creates a prompt that can be used with a
vision-capable model or OCR service.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import sys


@dataclass
class VisionImageRecord:
    page: int
    image_index: int
    path: str
    width: int
    height: int
    source_name: str


def import_pdf_reader():
    try:
        from pypdf import PdfReader  # type: ignore

        return PdfReader
    except Exception as exc:
        raise RuntimeError("pypdf is required to extract PDF images.") from exc


def import_pillow():
    try:
        from PIL import Image  # type: ignore

        return Image
    except Exception as exc:
        raise RuntimeError("Pillow is required to normalize extracted PDF images.") from exc


def resize_if_needed(image, max_side: int):
    if max_side <= 0:
        return image
    width, height = image.size
    largest = max(width, height)
    if largest <= max_side:
        return image
    scale = max_side / largest
    return image.resize((max(1, int(width * scale)), max(1, int(height * scale))))


def write_prompt(out_dir: Path, records: list[VisionImageRecord], language_hint: str) -> None:
    lines = [
        "# AI Vision OCR Prompt",
        "",
        "Use this prompt with a vision-capable model or OCR service.",
        "",
        "## Task",
        "",
        "Recognize the text in the attached page images. Preserve page order and mark page numbers.",
        "",
        "## Rules",
        "",
        "- Output one section per PDF page.",
        "- Use the format `## Page N` before each page's text.",
        "- Preserve headings, paragraph breaks, lists, and tables when visible.",
        "- Do not summarize during OCR.",
        "- Do not silently correct uncertain words; mark uncertain text with `[unclear: ...]`.",
        "- Ignore decorative borders unless they contain text.",
        "- If multiple images belong to the same PDF page, combine them in image order.",
        f"- Source language hint: {language_hint}.",
        "",
        "## Images",
        "",
    ]
    for record in records:
        lines.append(f"- Page {record.page}, image {record.image_index}: `{record.path}`")
    (out_dir / "vision_ocr_prompt.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_batches(out_dir: Path, records: list[VisionImageRecord], batch_size: int) -> None:
    if batch_size <= 0:
        batch_size = len(records) or 1
    batches = []
    for index in range(0, len(records), batch_size):
        part = records[index : index + batch_size]
        batches.append(
            {
                "batch": len(batches) + 1,
                "first_page": part[0].page if part else None,
                "last_page": part[-1].page if part else None,
                "images": [asdict(record) for record in part],
            }
        )
    (out_dir / "vision_ocr_batches.json").write_text(
        json.dumps(batches, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare PDF images for AI vision OCR.")
    parser.add_argument("pdf", help="Path to the PDF file.")
    parser.add_argument("--out", default="vision-ocr-input", help="Output directory.")
    parser.add_argument("--first-page", type=int, default=1, help="First 1-based page.")
    parser.add_argument("--last-page", type=int, default=None, help="Last 1-based page.")
    parser.add_argument("--max-side", type=int, default=2200, help="Resize longest side to this size. Use 0 to disable.")
    parser.add_argument("--batch-size", type=int, default=20, help="Images per suggested AI OCR batch.")
    parser.add_argument("--language-hint", default="Chinese Simplified and occasional English", help="Language hint for OCR.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    images_dir = out_dir / "page_images"
    images_dir.mkdir(parents=True, exist_ok=True)

    if not pdf_path.exists() or pdf_path.suffix.lower() != ".pdf":
        print(f"Input file was not found or is not a PDF: {pdf_path}", file=sys.stderr)
        return 2

    try:
        PdfReader = import_pdf_reader()
        import_pillow()
        reader = PdfReader(str(pdf_path))
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    page_count = len(reader.pages)
    last_page = args.last_page or page_count
    records: list[VisionImageRecord] = []

    for page_no in range(args.first_page, min(last_page, page_count) + 1):
        page = reader.pages[page_no - 1]
        for image_index, image_obj in enumerate(getattr(page, "images", []), start=1):
            try:
                image = getattr(image_obj, "image", None)
                if image is None:
                    from io import BytesIO
                    from PIL import Image  # type: ignore

                    image = Image.open(BytesIO(image_obj.data))
                image = resize_if_needed(image, args.max_side)
                image_path = images_dir / f"page-{page_no:03d}-image-{image_index:02d}.png"
                image.save(image_path, format="PNG")
                records.append(
                    VisionImageRecord(
                        page=page_no,
                        image_index=image_index,
                        path=str(image_path.relative_to(out_dir)),
                        width=image.size[0],
                        height=image.size[1],
                        source_name=getattr(image_obj, "name", ""),
                    )
                )
            except Exception as exc:
                error_record = {
                    "page": page_no,
                    "image_index": image_index,
                    "error": str(exc),
                }
                (out_dir / "vision_ocr_errors.jsonl").open("a", encoding="utf-8").write(
                    json.dumps(error_record, ensure_ascii=False) + "\n"
                )

    manifest = {
        "input": str(pdf_path),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "page_count": page_count,
        "first_page": args.first_page,
        "last_page": min(last_page, page_count),
        "image_count": len(records),
        "records": [asdict(record) for record in records],
    }
    (out_dir / "vision_ocr_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    with (out_dir / "vision_ocr_manifest.jsonl").open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")
    write_batches(out_dir, records, args.batch_size)
    write_prompt(out_dir, records, args.language_hint)
    print(out_dir / "vision_ocr_prompt.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
