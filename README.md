# PDF to TXT extractor

Usage:

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Place the PDF files you want to process into the `input` folder under the
   script directory (create it if needed), then run the extractor:

```bash
python extract_pdfs.py
```

The script will create a folder named `extracted_text` (or `extracted_text_1`, etc.)
and write one `.txt` file per PDF. Newlines are inserted after `.`, `!` and `?`.
