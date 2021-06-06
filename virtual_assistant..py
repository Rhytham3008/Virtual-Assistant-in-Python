import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

def record_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Let's talk!")
        audio = r.listen(source)

        data = ''

        try:
            data = r.recognize_google(audio)
            print(f"You said: {data} ")
        except sr.UnknownValueError:
            print("Didn't understand! want to try again")
        except sr.RequestError:
            print("Request Failed! Try again!")


    return data

def assistant_response(text):
    print(text)
    while True:
        try:
            obj = gTTS(text = text, lang = 'en', slow = False)
            obj.save('assistant_response.mp3')
            break
        except:
            print("Error! Trying Again...")

    playsound('assistant_response.mp3')

def wake_words(text):
    WAKE_WORDS = ["jarvis", "alexa", "friday", "vision", "ultron"]

    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False

def get_date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_name =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    return f"Today is {weekday}, {dayNum} of {month_name[monthNum -1]}"

def joker(text):
    jokes = ["Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them", "Question: Which of Santa's reindeer has the worst manners? Answer: RUDE-olph, of course", "Never trust math teachers who use graph paper. They're always plotting something.", "Question: What do you call friends who love math? Answer: algebros", "Question: What did one math book say to the other? Answer: Don't bother me I've got my own problems!", "Q. What did Neil Armstrong say when no one laughed at his moon jokes? A. 'I guess you had to be there'.", "Q. Which is closer, Florida or the moon? A. The moon. You can’t see Florida from here.", "Q. Why is a moon rock tastier than an Earth rock? A. It’s a little meteor.", "Q: Why didn't the sun go to college? A: Because it already had a million degrees!", "Q: What do planets like to read? A: Comet books!", "Q. Why couldn't the astronaut book a room on the moon? A. It was full!", "Q. What do scientists use to freshen their breath? A. Experi-mints!", "Q. Did you hear the one about the astronaut who stepped in gum? A. He got stuck in Orbit.", "Q. What does Earth say to tease the other planets? A: You guys have no life.", "Q. How do Earth, Saturn, and Neptune organize a party? A. They planet.", "Q. Where do astronauts like to party? A. The space bar", "Q. What do visitors to the International Space Station have to do before boarding? A. Pay the parking meteor.", "Q. How much room does a fungus need to grow? A. As mushroom as possible.", "Q. What did the astronomer's friends do after he didn't win the Nobel Prize? A. They gave him a constellation prize.", "Q. What did Neil Armstrong do after he stepped on Buzz Aldrin's toe? A. He Apollo-gized.", "Q. What do clouds do when they become rich? A. They make it rain!", "Did you hear about the chemist who was reading a book about helium? He couldn't put it down!", "What did the beach say when the tide came in? ... Long time no sea.", "Q: Why are chemists great for solving problems? A: They have all the solutions"]
    return random.choice(jokes)

def greeting(text):
    GREETINGS_INPUT = ['hi', 'hello', 'hey']

    GREETINGS_OUTPUT = ['hello sir', 'hi sir',]

    for word in text.split():
        if word.lower() in GREETINGS_INPUT:
            return random.choice(GREETINGS_OUTPUT)

    return ''

def getInfo(text):
    wordlist = text.split()

    for i in range(0, len(wordlist)):
        if i + 3 <= len(wordlist) -1 and wordlist[i].lower() == 'who' and wordlist[i+1].lower() == 'is':
            return f"{wordlist[i + 2]} {wordlist[i + 3]}"

while True:
    text = record_audio()

    response = ''

    if wake_words(text) == True:
        response = response + greeting(text)

        if 'date' in text:
            the_date = get_date()
            response = response + ' ' + the_date

        if 'who is' in text:
            person = getInfo(text)
            wiki = wikipedia.summary(person, sentences = 10)
            response = response + ' ' + wiki

        if 'joke' in text:
            laugher = joker(text)
            response = response + ' ' + laugher
        
        assistant_response(response)