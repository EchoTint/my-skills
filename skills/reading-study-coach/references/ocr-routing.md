# OCR Routing / OCR 路由

Resolve script examples from the actual absolute skill root, not the workspace
working directory. Quote paths and use temporary output storage. Follow
[source-intake.md](source-intake.md) for scope and external-upload boundaries;
image preparation is not itself completed OCR.

Use this reference when a PDF is scanned, image-based, mixed, or has low-quality text extraction.

## Core Principle

A scanned PDF is not directly readable as text. It must be handled through one of these routes:

1. Extract an existing text layer, if present.
2. Extract embedded page images and OCR them.
3. Render pages to images and OCR them.
4. Send page images to a vision-capable model or OCR service.

Do not say the PDF was fully read until one of these routes has produced usable page-level text or page-level visual reading notes.

## Default Route Order

### 1. Text Layer

First run `scripts/pdf_intake.py`.

If extraction quality is high, read the extracted text and preserve page references.

### 2. Windows Built-In OCR

On Windows, prefer this route before Tesseract when available:

```bash
python scripts/windows_ocr_pdf.py path/to/file.pdf --out work/windows-ocr --lang zh-Hans-CN
```

Use it when:

- The PDF is scanned or image-based.
- `pdf_intake.py` reports low extraction quality.
- The PDF contains extractable page images.
- Windows OCR has the needed language, such as `zh-Hans-CN` for Simplified Chinese.

This route avoids Poppler/pdftoppm and Tesseract. It uses `pypdf` and Pillow to extract embedded page images, then calls Windows built-in OCR.

### 3. AI Vision OCR

Use this when Windows OCR is unavailable, too inaccurate, or the user explicitly wants a stronger OCR/visual reading path.

Prepare images:

```bash
python scripts/prepare_vision_ocr.py path/to/file.pdf --out work/vision-ocr-input
```

Then use a vision-capable model or OCR service on the exported images with `vision_ocr_prompt.md`.

Important:

- Tell the user whether page images may leave the local machine.
- Batch long books; do not send hundreds of pages at once.
- Preserve page numbers and mark uncertain text.
- Do OCR first; do not summarize while recognizing text.

### 4. Tesseract / Poppler Fallback

Use this when Windows OCR is unavailable and local open-source OCR tools are installed:

```bash
python scripts/ocr_pages.py path/to/file.pdf --out work/tesseract-ocr
```

This requires:

- `pdftoppm` from Poppler
- `tesseract`
- the relevant language data, such as `chi_sim`

## Evidence Policy After OCR

After any OCR route, label evidence status:

- **Confirmed**: visible in OCR text or page image.
- **Low-confidence OCR**: OCR text is present but noisy, broken, or likely wrong.
- **Reasoned inference**: inferred from structure or context, not directly confirmed by OCR.
- **Needs rereading**: OCR could not resolve the page, passage, table, or figure.

## When OCR Is Still Not Enough

OCR may fail on:

- old scans
- skewed pages
- dense tables
- diagrams
- formulas
- marginalia
- mixed Chinese and English
- decorative title pages

For those pages, use page-image visual reading and explicitly mark uncertainty.

## Chinese Output Note

Windows OCR often inserts spaces between Chinese characters. Clean those spaces before using the text for reading analysis, but do not silently rewrite uncertain words into polished prose.
