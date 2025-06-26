import os
import io
import markdown
from xhtml2pdf import pisa


def convert_md_to_pdf(md_path, pdf_path):
    """
    Convert a markdown file at md_path to a PDF file at pdf_path.
    Returns True on success, False on failure.
    """
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    # Convert markdown to HTML
    html_body = markdown.markdown(md_text)
    # Wrap in basic HTML document
    html = f"""<html><head><meta charset=\"utf-8\"></head><body>{html_body}</body></html>"""
    # Generate PDF
    with open(pdf_path, 'wb') as pdf_file:
        pisa_status = pisa.CreatePDF(io.StringIO(html), dest=pdf_file)
    return not pisa_status.err


def crawl_and_convert(directory):
    """
    Walk through the given directory, find all .md files and convert them to PDF.
    """
    for root, _, files in os.walk(directory):
        for name in files:
            if name.lower().endswith('.md'):
                md_path = os.path.join(root, name)
                pdf_path = os.path.splitext(md_path)[0] + '.pdf'
                print(f"Converting {md_path} -> {pdf_path}")
                success = convert_md_to_pdf(md_path, pdf_path)
                if not success:
                    print(f"Failed to convert {md_path}")


if __name__ == '__main__':
    # Crawl the docs/ directory relative to this script
    crawl_and_convert(os.path.join(os.path.dirname(__file__), 'docs'))
