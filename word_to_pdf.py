import aspose.words as aw

def convert_word_pdf():
    doc=aw.Document('IPv6 address.docx')
    doc.save('IPv6 address.pdf')

convert_word_pdf()