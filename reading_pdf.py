from PyPDF2 import PdfReader


reader = PdfReader("stowarzyszenie.pdf")
print(len(reader.pages))

page = reader.pages[0]

text = page.extract_text()

print(text)