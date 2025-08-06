import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from pypdf import PdfReader, PdfWriter

current_dir = os.getcwd()
os.makedirs("pdfs", exist_ok=True)
pdf_folder = os.path.join(current_dir, "pdfs")

# Function to create a PDF with automatic line breaks
def create_pdf_with_wrapped_text(filename, text, max_width=80):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    lines = simpleSplit(text, 'Helvetica', 12, width - 200)
    y = 750
    for line in lines:
        c.drawString(100, y, line)
        y -= 20
        if y < 50:
            c.showPage()
            y = 750
    c.save()

# Example usage: create a PDF with wrapped text
long_text = (
    "Hello, Genius! This is a new PDF. "
    "You can add multiple lines, shapes, and more. "
    "This is a very long line that should automatically wrap to the next line if it exceeds the page width. "
    "Keep adding more text to see the effect of line wrapping in the generated PDF file."
)
create_pdf_with_wrapped_text(os.path.join(pdf_folder, "new_file.pdf"), long_text)

# Merge PDFs
pdffile1 = os.path.join(pdf_folder, "sample-1.pdf")
pdffile2 = os.path.join(pdf_folder, "sample-2.pdf")
pdfs = [pdffile1, pdffile2, os.path.join(pdf_folder, "new_file.pdf")]

writer = PdfWriter()

for pdf in pdfs:
    reader = PdfReader(pdf)
    for i, page in enumerate(reader.pages):
        # Example: Rotate every second page by 90 degrees
        # if i % 2 == 1:
        #     page.rotate(90)
        # Example: Crop the page (reduce margins)
        page.mediabox.lower_left = (50, 50)
        page.mediabox.upper_right = (500, 750)
        writer.add_page(page)

# Save merged PDF in pdfs folder
merged_pdf_path = os.path.join(pdf_folder, "merged_output.pdf")
with open(merged_pdf_path, "wb") as f:
    writer.write(f)

print(f"Merged PDF created: {merged_pdf_path}")