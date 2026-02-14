#!/usr/bin/env python3
"""Extract text from all PDF files in the current directory.

Creates an output folder `extracted_text` (or `extracted_text_1`, `_2`, ...) and
writes one .txt file per PDF. Inserts a newline after '.', '!' and '?'.
"""
import os
import re
from pdfminer.high_level import extract_text


def make_output_dir(base_name="extracted_text"):
    candidate = base_name
    i = 1
    while os.path.exists(candidate):
        candidate = f"{base_name}_{i}"
        i += 1
    os.makedirs(candidate)
    return candidate


def normalize_text(text: str) -> str:
    # Insert a newline after '.', '!' or '?' when followed by whitespace
    text = re.sub(r'([.!?])\s+', r'\1\n', text)
    # Collapse excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + "\n"


def main():
    input_dir = "input"
    if not os.path.exists(input_dir):
        print(f"Input directory '{input_dir}' does not exist. Creating it now.")
        os.makedirs(input_dir)
        print(f"Place your PDF files into the '{input_dir}' folder and re-run the script.")
        return

    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print(f"No PDF files found in the '{input_dir}' directory.")
        return

    out_dir = make_output_dir("extracted_text")
    print(f"Writing extracted text files to: {out_dir}")

    for pdf in pdf_files:
        pdf_path = os.path.join(input_dir, pdf)
        try:
            text = extract_text(pdf_path)
        except Exception as e:
            print(f"Error extracting '{pdf}': {e}")
            continue

        processed = normalize_text(text)
        txt_name = os.path.splitext(os.path.basename(pdf))[0] + ".txt"
        txt_path = os.path.join(out_dir, txt_name)
        try:
            with open(txt_path, "w", encoding="utf-8") as out:
                out.write(processed)
            print(f"Wrote: {txt_path}")
        except Exception as e:
            print(f"Error writing '{txt_path}': {e}")


if __name__ == "__main__":
    main()
