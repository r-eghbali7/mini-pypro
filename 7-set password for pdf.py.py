from PyPDF2 import PdfWriter, PdfReader
import getpass

def protect_pdf(input_pdf_path, output_pdf_path):
    input_pdf = PdfReader(input_pdf_path)
    output_pdf = PdfWriter()

    for page_number in input_pdf.pages:
        output_pdf.add_page(page_number)

    password = getpass.getpass(prompt="Enter password: ")
    output_pdf.encrypt(password)
    with open(output_pdf_path, "wb") as output_pdf_file:
        output_pdf.write(output_pdf_file)
    
    print(f"PDF protected successfully created name: {output_pdf_path} !")

protect_pdf("aa.pdf", "aa_protected.pdf")
