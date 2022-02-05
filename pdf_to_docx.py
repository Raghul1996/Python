import aspose.words as a

def convert_pdf_to_docx():
    d=a.Document('Raghul\'s resume.pdf')
    d.save('Raghul\'s resume.docx')

convert_pdf_to_docx()

