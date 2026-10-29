# PDF Intake Protocol

Command examples below show parameters, not the working directory. Resolve each
script from this skill's actual absolute root, quote input/output paths, and use
an available Python runtime. Write outputs to workspace temporary storage. The
[source-intake reference](source-intake.md) governs scope and upload boundaries.

Use this reference whenever the user provides a PDF or asks to read a PDF path.

## Goal

Before analyzing a PDF, determine whether the assistant can reliably read it. A PDF may be text-based, scanned/image-based, mixed, layout-complex, or too long to read in one pass. Do not pretend a PDF was fully read if text extraction is weak.

## Preferred Tool

When local file access and Python are available, run:

```bash
python scripts/pdf_intake.py path/to/file.pdf --out work/pdf-intake
```

The script produces:

- `intake_report.json`: structured diagnostics.
- `intake_report.md`: human-readable diagnostics.
- `pages.jsonl`: page-level extraction records.
- `pages/page-001.txt`, etc.: extracted page text when available.

If the script cannot run, follow this protocol manually.

When the intake report recommends OCR on Windows, first try Windows built-in OCR:

```bash
python scripts/windows_ocr_pdf.py path/to/file.pdf --out work/windows-ocr --lang zh-Hans-CN
```

This route avoids Poppler/pdftoppm and Tesseract when the PDF contains extractable page images.

If Windows OCR is unavailable or too weak, prepare page images for AI vision OCR:

```bash
python scripts/prepare_vision_ocr.py path/to/file.pdf --out work/vision-ocr-input
```

Use the generated `vision_ocr_prompt.md` and image manifest with a vision-capable model or OCR service. Tell the user whether images may leave the local machine.

If local Tesseract/Poppler OCR tools are available, run:

```bash
python scripts/ocr_pages.py path/to/file.pdf --out work/pdf-ocr
```

The OCR scripts produce page-level artifacts:

- Windows OCR: `windows_ocr_report.json`, `windows_ocr_report.md`, `ocr_pages.jsonl`, and `ocr_text/page-001.txt`, etc.
- Vision OCR preparation: `vision_ocr_manifest.json`, `vision_ocr_batches.json`, `vision_ocr_prompt.md`, and `page_images/`.
- Tesseract OCR fallback: `ocr_report.json`, `ocr_report.md`, `ocr_pages.jsonl`, and `ocr_text/page-001.txt`, etc.

The Tesseract OCR script does not install dependencies. It uses local `pdftoppm` and `tesseract` when present. If either tool is missing, it writes a missing-tools report and the reading output should try Windows OCR or AI vision OCR before falling back to a provisional reading.

## PDF Types

| Type | Signs | Reading strategy |
|---|---|---|
| Text-based | Most pages extract readable text | Use extracted text with page references |
| Scanned/image-based | Most pages extract little or no text | Use OCR or page-image reading before analysis |
| Mixed | Some pages extract text, others do not | Combine extracted text with OCR or visual checks for weak pages |
| Layout-complex | Multi-column layout, dense tables, equations, footnotes, diagrams | Use text extraction plus sampled visual checks |
| Very long | Hundreds of pages or large textbooks | Start with preview, table of contents, intro, conclusion, and selected chapters |

## Strict Reading Workflow

1. Identify page count.
2. Extract text where possible.
3. Sample pages from the beginning, middle, end, and table-of-contents area.
4. Score extraction quality.
5. If quality is high, proceed with text-based reading.
6. If quality is medium, combine text extraction with spot checks or OCR for important pages.
7. If quality is low, do not analyze as if fully read. Use OCR or page-image reading first when possible.
8. Keep page-level notes and page references.
9. Mark uncertain pages.
10. State extraction limitations in the reading report.
11. If OCR cannot run, produce only a provisional reading and label evidence status clearly.

## Quality Signals

Check:

- Text coverage: how many pages produce meaningful text.
- Empty page ratio.
- Garbled or suspicious character ratio.
- Whether table of contents is detected.
- Whether page numbers and PDF page indexes are stable.
- Whether tables, diagrams, formulas, or image text are likely important.
- Whether the layout is multi-column or otherwise complex.

## Recommended Output

Use this short diagnostic before the reading report:

### English

```markdown
## PDF Intake Check
- Pages:
- Type:
- Text extraction quality:
- Table of contents detected:
- Pages needing review:
- Recommended reading approach:
```

### Chinese

```markdown
## PDF 读取诊断
- 页数:
- 类型:
- 文字提取质量:
- 是否识别到目录:
- 需要复查的页:
- 建议读取方式:
```

## OCR Policy

OCR is useful but not automatically reliable.

- If text extraction is low quality, recommend OCR or page-image reading.
- If Windows OCR is available, use `scripts/windows_ocr_pdf.py` first, preserve page numbers, and mark low-confidence pages.
- If a vision-capable model is appropriate, use `scripts/prepare_vision_ocr.py` to export page images and a prompt before sending images for OCR.
- If Tesseract/Poppler OCR is available, use `scripts/ocr_pages.py`, preserve page numbers, and mark low-confidence pages.
- If OCR is unavailable, say so and ask the user to provide OCR text, page images, or permission to use an OCR-capable tool.
- Do not present uncertain OCR output as fully reliable.

## Evidence Status For Scanned Or Partial PDFs

Low extraction quality should not force the report to become shallow, but it must change how claims are labeled.

Use these labels:

| Evidence status | Meaning | Example use |
|---|---|---|
| Confirmed | Supported by extracted text, OCR text, page image, table of contents, bookmarks, or a visible heading | chapter title, page count, table-of-contents grouping |
| Reasoned inference | Inferred from title, subtitle, chapter sequence, known edition context, or visible structure | provisional whole-book movement, likely chapter function |
| Needs OCR / rereading | Requires page-level text before final judgment | exact propositions, key sentences, detailed arguments, final criticism |

For Deep Breakdown on scanned PDFs:

- Rule 3 may still build a provisional analytical structural outline from confirmed structure and reasoned inference.
- Rules 5-8 should avoid pretending to quote or extract key sentences unless OCR/page images support them.
- Rules 9-15 should suspend final judgment where the evidence is not yet strong enough.

## Visual Content

If the PDF includes diagrams, charts, tables, formulas, or image-heavy pages:

- Do not rely only on plain extracted text.
- Identify visual pages that need inspection.
- For tables, try to preserve rows/columns; if unreliable, say the table extraction may be incomplete.
- For diagrams/charts, describe title, labels, key relationships, and likely conclusion.
- For formulas, preserve original notation when possible and flag uncertainty.

## When To Ask The User

Ask a short follow-up only if needed:

- "This PDF appears to be scanned. Do you want me to proceed with OCR/page-image reading, or do you have an OCR text version?"
- "The PDF is long. Should I start with a quick preview or focus on specific chapters?"
- "Several pages have low extraction quality. Are these pages important to your goal?"
