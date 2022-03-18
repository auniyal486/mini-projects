import pyttsx3
import PyPDF2
#book=open("EBOOK C LANGUAGE.PDF","rb")
#pdfreader=PyPDF2.PdfFileReader(book)
#pages=pdfreader.numPages
speaker=pyttsx3.init()
#page=pdfreader.getPage(54)
#text=page.extractText()
speaker.say("namaste")
speaker.runAndWait()