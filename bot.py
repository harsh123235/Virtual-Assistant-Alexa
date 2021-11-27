import speech_recognition as sr
# from gtts import gTTS
import pyttsx3
# import pyaudio
import wikipedia
import pywhatkit
import datetime
import pyjokes
import webbrowser
import os

listener = sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("...listeninng..")
            listener.adjust_for_ambient_noise(source)
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()

            if 'alexa' in command:
                command=command.replace('alexa','')
                talk(command)
                print(command)
    except:
        pass
    return command

def wishme():
    hour=int(datetime.datetime.now)
    if hour>0 and hour<12:
        talk("good morning")
    elif hour<12 and hour>18:
        talk("good afternoon")
    else:
        talk("good evening")
    talk("hey i am voice assistant what can i help you")
        
def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        print('playing..')
        talk('playing')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I,%M,%S')
        print(time)
        talk("current time is "+time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'date' in command:
        talk('sorry i have mingle')
        print('sorry i have mingle')
        
    elif 'open youtube' in command:
        webbrowser.open_new_tab("www.youtube.com")
    elif 'open google' in command:
        webbrowser.open_new_tab("www.google.com")
    
    elif 'open' in command:
        path="D:\\python2.0\\alexxa"
        os.startfile(path)
    
        
    elif 'stop' in command:
        exit()

    else:
        talk('say it again')
        print('say it again')



wishme()
while True:
    run_alexa()

