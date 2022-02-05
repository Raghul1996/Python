import aspose.words as w
from pathlib import Path

class convert:
    def __init__(self,sourcefile,destinationformat):
        self.sourcefile=sourcefile
        self.destinationformat=destinationformat

    def docx_to_pdf(self):
        file_name=Path(self.sourcefile).stem
        doc_r=w.Document(self.sourcefile)
        doc_r.save(file_name+"."+self.destinationformat)


ad=convert(r'E:\Raghul\VS Codes\Statement.pdf','docx')
ad.docx_to_pdf()

