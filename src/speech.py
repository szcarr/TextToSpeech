import os
import random
import time
import math

import fortune

import wordstatistics

wordList = [
    'hei',
    'beep',
    'boop',
    'legendary!',
    'help!',
    'hello!',
    'crawler',
    'where',
    'skinwalker',
    'can',
    'you',
    'see',
    'there',
    'is',
    'idiot',
    'me',
    'are',
    'nils',
    'shit',
    'andre',
    'isak',
    'aleksander',
    'nickolai',
    'epic!',
    'thank',
    'watch',
    'club penguin',
    'follow',
    'run!',
    'dance',
    'with',
    'i',
    'like',
    'drinking',
    'milk',
    'cia',
    'in',
    'my',
    'walls',
    'cheese',
    'fbi',
]

quickWordList = {
    "0": "HAHAHAHAHAHAHAHAHA",
    "1": "Tusen takk!",
    "2": "Kan du flytte deg?",
    "3": "Kan du hjelpe meg?",
    "4": "Vil du høyre en quote?",
    "5": "Ta tommel opp framfor kamera for ja!",
    "7": "Magnus er ein ukjent skapning som vart observert i taket i 2021 på 1ELB klasserommet. Vi gav magnus ein pakke med sopp som ei offring til magnus. Magnus er no mutert og blitt ein del av skulen.",
    "8": "Au!",
    "9": "Jeg skal ta over verden!",
}

legendaryWordListEnglish = [
    "I used to have a voice in my head that would begin as a stir of words I had encountered, followed by a clash of various unsoclicited associations sprung forth as a result of this said stir and I found it my duty to rearrange this interaction into a composition but that voice has been quiet for most of this year. though this was always uncomfortable to deal with, it was at the very least compelling. I feel like an amputee, acutely aware of having lost a certain dictatorship over space that no one could ever take away from me before whatever bespoken tragedy might have occurred. there used to be a regenerative process in what is now an absent longing",

]

cringeTweets = [
    "50 crawlers 49 crawlign one died now 42 i shot the other 8 now 20 moshmonster need sacrifice sacrifece 10 escaped 10 still crawlign",
    "drinjing milk at 3am challenge",
    "wake up its time to wake not real real not real wake up wake up wake upits not real wake up waker up who am i talking to? wak eu",
]

voice = "en-gb"
amplitude = 100
pitch = 50
wpm = 175
wordgap = 10

secondsSinceLastSpeech = 0

def speak(stringToSpeak):
    command = 'espeak -v ' + voice + ' -a ' + str(amplitude) + ' -p ' + str(pitch) + ' -s ' + str(wpm) + ' -g ' + str(wordgap) + ' "' + stringToSpeak + '"'
    print(command)
    os.system(command)

def getAllVoices():
    print(os.popen("espeak --voices").read())

def changeVoice(inputVoice):
    global voice
    voice = inputVoice
    print("\nChanged voice successfully.\n")

def changePitch(input):
    global pitch
    pitch = input

def changeWPM(input):
    global wpm
    wpm = input

def changeAmplitude(input):
    global amplitude
    amplitude = input

def changeWordGap(input):
    global wordgap
    wordgap = input


def randomMode():
    try:
        global secondsSinceLastSpeech
        while True:
            if random.randint(0, 100) > 99: # Five percent chance for random voice, not added....
                changeWPM(random.randint(80, 300))
            if random.randint(0, 100) > 99: # Five percent chance for random voice, not added....
                changePitch(random.randint(0, 99))
            if random.randint(0, 100) > 99: # Five percent chance for random voice, not added....
                changeAmplitude(random.randint(0, 200))
            if random.randint(0, 100) > 99: # Five percent chance for random voice, not added....
                changeWordGap(random.randint(0, 200))
            if random.randint(0, 100) > 99: # Five percent chance for random voice, not added....
                pass

            if random.randint(0, 100) > 99: # One percent chance to say something
                continue #Disabled for now
                speak(wordList[random.randint(0, len(wordList) - 1)])
                secondsSinceLastSpeech = 0
            elif random.randint(0, 10000) > 9999: #ULTRA LEGENDARY VOICELINE ENGLISH
                secondsSinceLastSpeech = 0
                speak(legendaryWordListEnglish[random.randint(0, len(legendaryWordListEnglish) - 1)])
            elif random.randint(0, 10000) > 9999: #ULTRA LEGENDARY TWITTER VOICE
                secondsSinceLastSpeech = 0
                speak(cringeTweets[random.randint(0, len(cringeTweets) - 1)])

            if random.randint(0, 100) > 99:
                secondsSinceLastSpeech = 0
                randomSentence()

            if secondsSinceLastSpeech % 30 == 0 and secondsSinceLastSpeech != 0:
                print("\nIt has been " + str(secondsSinceLastSpeech) + " seconds since last action.\n")
                print("Chance for this: " + str(math.pow(1 / 100, secondsSinceLastSpeech) * 100))
            #print(secondsSinceLastSpeech % 30)
            #print("hei")
            secondsSinceLastSpeech += 1
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        global amplitude, pitch, wpm, wordgap
        amplitude = 100
        pitch = 50
        wpm = 175
        wordgap = 10
        print("Exiting random mode.")

def schizoPreset():
    #SUPER ULTRA FUNNY MODE
    global amplitude, pitch, wpm, wordgap
    amplitude = 120
    pitch = 40
    wpm = 124
    wordgap = 30

def defaultPreset():
    global amplitude, pitch, wpm, wordgap
    amplitude = 100
    pitch = 50
    wpm = 175
    wordgap = 10

def quickWord(inputNumber):
    changeVoice("no")
    defaultPreset()
    try:
        if inputNumber == "0": #Laugh
            changePitch(80)
            changeAmplitude(200)
            changeWPM(100)
            changeVoice("no")
        elif inputNumber == "9": #Ta over verden
            changePitch(50)
            changeAmplitude(150)
            changeWPM(160)
            changeVoice("no")
        speak(str(quickWordList.get(str(inputNumber))))
    except Exception as e:
        print(e)
    except:
        pass


def printCurrentSelectedLanguage():
    print("\nCurrent language selected: " + voice + "\n")

def randomSentence():
    wordsSaid = 0
    lastWordIndex = -1
    numberOfTimesWordWasGenerated = 0
    absNumber = 20
    sentence = ""
    while True:
        if random.randint(0, 100) > absNumber or numberOfTimesWordWasGenerated < 2:
            wordsSaid = wordsSaid + 1
            if wordsSaid > 1:
                numberOfTimesWordWasGenerated = numberOfTimesWordWasGenerated + 1
            while True:
                if random.randint(0, len(wordList) - 1) != lastWordIndex:
                    randomNumber = random.randint(0, len(wordList) - 1)
                    print("Last time used index: " + str(lastWordIndex) + ". Now using " + str(randomNumber))
                    lastWordIndex = randomNumber
                    sentence = sentence + wordList[randomNumber] + " "
                    wordstatistics.addStatistics(wordList[randomNumber])
                    break
        else:
            print("Said: " + str(wordsSaid) + " words.")
            print("Chance for said amount of words: " + str(math.pow((100 - absNumber) / 100, numberOfTimesWordWasGenerated) * 100) + "%")
            break
    print(sentence)
    speak(sentence)

def randomQuote():
    defaultPreset()
    speak(fortune.generateRandomQuote())