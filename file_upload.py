import os
from pathlib import Path
fileitem=form['filename']
if fileitem.filename:
    fn=Path(fileitem.filename).stem
    open(fn,'wb').write(fileitem.file.read())
