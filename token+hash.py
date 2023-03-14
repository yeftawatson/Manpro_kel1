from nltk.tokenize import sent_tokenize
from docx import Document
import hashlib

#ambil isi dokumen
document = Document('tes.docx')
# docume

paragraf_docx = ""
for paragraph in document.paragraphs:
    # print(paragraph.text)
    paragraf_docx += paragraph.text.lower()

arrTeks = []
arrResHash = []
for i in sent_tokenize(paragraf_docx):
    print(i)
    i = i.replace(" ", "")
    arrTeks.append(i)
    i = hashlib.sha256(i.encode())
    i = i.hexdigest()
    arrResHash.append(i)

print(arrTeks)
print(arrResHash)

