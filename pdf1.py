import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


pr=extract_text_from_pdf(r"C:\Users\Srijan\Downloads\5013001190 (1).pdf")
print(pr)
        
