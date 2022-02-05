from PIL import Image
from pathlib import Path

class convert:
    def __init__(self,source_img_path,destimgformat):
        self.source_image_path=source_img_path
        self.dest_img_format=destimgformat

    def convert_image(self):
        im=Image.open(self.source_image_path)
        #im.show()
        file_name=Path(self.source_image_path).stem
        #file_name=file_name+"."+self.dest_img_format
        im.save(file_name+"."+self.dest_img_format)
        im.show()

ab=convert('E:\\Raghul\\VS Codes\\new.jpg','png')
ab.convert_image()
