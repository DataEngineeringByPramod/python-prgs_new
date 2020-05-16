from PyPDF2 import PdfFileMerger
import os

#path = '\C:\pdfs'
pdf_files = ['1.pdf', '2.pdf']
merger = PdfFileMerger()
for files in pdf_files:
    merger.append(files)
if not os.path.exists('merged.pdf'):
    merger.write('merged.pdf')

merger.close()
