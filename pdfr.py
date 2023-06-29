from pyttsx3 import*
import PyPDF2

def speak(text):
    engine = Engine()
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')  
    engine.setProperty('rate', 125) 
    engine.say(text)
    engine.runAndWait()

    
pdf = open('python.pdf', 'rb')
pdfr = PyPDF2.PdfReader(pdf)
length = len(pdfr.pages)
for i in range(1,length):
    page = pdfr.pages[i]
    text = page.extract_text()
    print(text)
    speak(text)