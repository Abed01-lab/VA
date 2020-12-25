# VA body
import speech_recognition as sr 
import os
from gtts import gTTS
from playsound import playsound

# Features
import datetime

# data
from whatis import whatis

# global object
r = sr.Recognizer()                                                                                   

# response to the audio
def response(data):
    data = r.recognize_google(data)
    print(data)
    if "what is" in data:
        words = data.split(' ')
        itemList = []
        for word in words:
            if word != "what" and word != "is":
                print(word)
                itemList.append(word)
                item = getItem(itemList)
        if whatis[item]:
            voice(whatis[item])
        else:
            voice("I do not know")

def voice(data):
    tts = gTTS(text = data, lang='en')
    tts.save("Voice.mp3")
    playsound("Voice.mp3")
    os.remove("Voice.mp3")

def getItem(array):
    item = ""
    for word in array:
        item += word + " "
    return item.strip()
    
# get audio from the microphone                                                                       
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)
    response(audio)


try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
        