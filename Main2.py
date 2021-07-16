import pyttsx3
import speech_recognition as sr
import pywhatkit as py
import datetime as dt
import wikipedia
import pyjokes
from weather import Weather
import requests
import os
import time as t # to avoid confusion in functions
#for improving performance manually works really well
import gc
from tqdm.auto import tqdm
gc.collect()
def loading():
    print("Loading Modules...")
    for i in tqdm(range(100)):
        t.sleep(0.003)
def hello():
    os.system('cls')
    filenames=["Hello1.txt","Hello2.txt"]
    frames=[]

    for name in filenames:
        with open(name,"r",encoding='utf8') as f:
            frames.append(f.readlines())
        for i in range(3):
            for frame in frames:
                print("".join(frame))
                t.sleep(0.5)
                os.system('cls')

def wishme():
    loading()
    
    hello()
    hour=dt.datetime.now().hour
    if hour>=0 and hour<12:
        talk("'Good' Morning!")
    elif hour>=12 and hour<18:
        talk("'Good' Afternoon!")
    else:
        talk("'Good' Evening!")
    del hour
    gc.collect()

def talk(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


wishme()
engine.say("I'm 'Jarvis', How may I help you?")
engine.runAndWait()
def birthday():
    pass
def search(command):
    py.search(command)
def what_can_i_do():
    print("\n")
    talk("I can assist you in many commands! like...")
    print("To know about Weather")
    print("Open Browsers")
    print("Date,time")
    print("Play songs on youtube")
    t.sleep(5)
def time():
    time = dt.datetime.now().strftime('%I:%M %p')
    print(time)
    talk('current time is ' + time)
def date():
    date = dt.datetime.now()
    print(f"today is {date.strftime('%d')} of {date.strftime('%B')}  {date.strftime('%Y')}")
    talk(f"today is {date.strftime('%d')} of {date.strftime('%B')}  {date.strftime('%Y')}")
def week():
    date = dt.datetime.now()
    print(f"Today is {date.strftime('%A')}")
    talk(f"Today is {date.strftime('%A')}")
def whois(command):
    try:
        info = command.replace('who is', '')
        talk('searching results for ' + info + 'on wikipedia')
        info = wikipedia.summary(info, sentences=1)
        print(info)
        talk('According to "Wikipedia "')
        talk(info)
        return False
    except wikipedia.exceptions.PageError as e:
        talk('I didnt find him on "Wikipedia"')
        talk('Instead, I found This on web')
        search(command)
        return True
def loveyou():
    print("'I am a machine! 1 0 1 1 1 0 1 0 1 just kidding'")
    talk("I am a 'machine'! 1 0 1 1 1 0 1 0 1! just kidding")
def single():
    print("I'm happy to say I feel whole on my own")
    print("Plus, I never have to share my icecreams")
    talk("I'm happy to say I feel whole on my own, Plus, I never have to share my icecreams")
    return 0
def joke():
    talk(pyjokes.get_joke())
def play(command):

    video = command.replace('play', '')
    talk('Playing'+ video)
    print("\n"+"playing"+video)
    py.playonyt('\nplaying'+ video)
def weather():
    res= requests.get('https://ipinfo.io/')
    data= res.json()
    city=data['city']
    weather = Weather(temperature_unit='Celsius')
    current_weather = weather.fetch_weather(city=city, only_temp=False)
    temperature=current_weather['Temperature: ']
    temperature.replace('C','Celsius')
    description=current_weather['Description: ']
    print(current_weather)
    print(f"The temperature is {temperature} with {description}")
    talk(f"The temperature is {temperature} with {description}")


def Jarvis_command():
    try:
        os.system('cls')
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            listener.dynamic_energy_threshold = 3000
            voice = listener.listen(source)

            command = listener.recognize_google(voice)
            os.system('cls')
            if 'Jarvis' in command:
                command=command.replace('Jarvis', '')
    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Network error.")

    try:
        print(command)
        return command
    except UnboundLocalError:
        run_Jarvis()



def run_Jarvis():
    command=Jarvis_command()
    #commands That open in Default Web Browser
    try:
        if 'play' in command:
            play(command)
            print('Paused, Hit Enter to Continue')
            x=str(input())
            if x=='':
                return 0
            return 1
        elif 'song' in command or 'songs' in command:
            play('Top 50 This Week & top 100 songs ')
            print('Paused, Hit Enter to Continue')
            x = str(input())
            if x == '':
                return 0
            return 1
        elif 'search' in command:
            command=command.replace('search','')
            talk("Searching" + command)
            search(command)
            print('Paused, Hit Enter to Continue')
            x = str(input())
            if x == '':
                return 0
            return 1
        elif 'who is' in command:
            a=whois(command)
            if a==True:
                print('Paused, Hit Enter to Continue')
                x=str(input())
                if x == '':
                    return 0
                return 1
            else:
                pass
        elif 'search' in command:
            command=command.replace('open','')
            talk("searching"+command+"in default webbrowser")
            search(command)
            print('Paused, Hit Enter to Continue')
            x = str(input())
            if x == '':
                return 0
            return 1
        elif 'time' in command:
            time()
        elif 'date' in command:
            date()
        elif 'week' in command or 'day' in command:
            week()
        elif 'weather' in command:
            talk("Searching for weather")
            weather()
        elif 'love you' in command:
            loveyou()
        elif 'are you single' in command:
            single()
        elif 'joke' in command:
            joke()
        elif 'hello' in command:
            talk("it's really good to hear from you, I hope you're doing well!")
        elif 'what can you' in command or "what's your job"in command or "what will you" in command:
            what_can_i_do()
        elif 'introduce'in command or 'who are you' in command or 'what are you' in command or "your name" in command:
            talk("I am 'Jarvis'!, your personal assistant, Nice to meet you \n ")
        elif  'you' in command and 'live'in command or 'your'in command and 'home' in command:
            talk("I live in your computer and cloud, its really magical!")
        elif 'built' in command and 'you' in command or 'your'in command and'maker' in command or 'made you' in command or 'creator' in command and 'your'in command:
            talk("Thanks! \n I was 'developed' with the help of various webpages, Youtube tutorials and of course, 'stack overflow'! plus, a human")
        elif 'thanks' in command:
            talk("'Have A great day'")
            return 1
        elif ' my birthday' in command():
            birthday()

        else:
            print("Oops, I am not yet programmed for that!")
            talk("Oops, I am not yet programmed for that!")
            what_can_i_do()

    except TypeError:
        talk("Oops, I am not yet programmed for that!")
        run_Jarvis()
    del command
    gc.collect()
X=0

while True:
    if X!=1:
        X = run_Jarvis()
    else:
       break
