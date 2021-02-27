import speech_recognition as sr
import pyttsx3
import pywhatkit          #due this we can access youtube and other
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices =engine.getProperty('voices')         #add this line to change voice to female voice
engine.setProperty('voice', voices[1].id)    #[1].id is female voice

def talk(text):
    engine.say(text)
    engine.runAndWait()





def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis'in command:  #if jarvis is in your speech then only it will listen to you
                command = command.replace('jarvis', '')       #this will not print jarvis
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)      #if play is in command then i will say palying
        pywhatkit.playonyt(song)    #yt=youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('current time is' + time)  #time
    elif 'love you' in command:
        talk('am all yours from the day you brought me home from shop' )
    elif 'are you single' in command:
        talk('am in relationship with wifi')
    elif 'you born' in command:
        talk(' abhishek"s efforts bringed me here')
    elif 'tell me a joke' in command:
        talk(pyjokes.get_jokes())
    elif 'who is'  in command:
        person = command.replace('who is' ,'')
        info = wikipedia.summary(person, 1)    #1 means it gives only one line of result on wekepedia
        print(info)
        talk(info)
    else:
        talk('sorry,what did you say i cant hear you properly')

while True:
    run_jarvis()



