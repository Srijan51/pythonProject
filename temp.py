from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    txt= extract_text(pdf_path)
    return txt

pr=extract_text_from_pdf(r"C:\Users\Srijan\Downloads\in.gov.abc-ABCID-990902352867.pdf")
print(pr)