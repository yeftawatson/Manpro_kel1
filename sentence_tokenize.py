from nltk.tokenize import sent_tokenize
from docx import Document

#ambil isi dokumen
document = Document('tes.docx')

text = "God is Great! I won a lottery."
# print(sent_tokenize(text))
# for i in sent_tokenize(text):
#     print(i)

paragraf_docx = ""
for paragraph in document.paragraphs:
    # print(paragraph.text)
    paragraf_docx += paragraph.text

paragraf_docx = paragraf_docx.lower()

for i in sent_tokenize(paragraf_docx):
    print(i)
