"""
读取PDF文件
https://github.com/py-pdf/PyPDF2 
"""

from PyPDF2 import PdfFileReader

with open('./res/Docker入门教程.pdf', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(5)
    print(current_page)
    print(current_page.extractText())