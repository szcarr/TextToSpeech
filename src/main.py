import time
import os

import speech
import threadedspeech
import wordstatistics #
import livespeechclient

exitProgram = False

modeList = {
    "mic": "mic | Requests microphone input from client | Syntax: mic",
    "streammic": "Stream microphone | Requests microphone input from client and streams it (ish) | Syntax: streammic",
    "s": "s | Transforms text to speech | Syntax: s <string>",
    "cv": "cv | Changes voice. See list from the 'vh' command | Syntax: cv <language code>",
    "delstats": "delstats | Resets statistics | Syntax: delstats",
    "vh": "vh | See all voice languages | Syntax: vh",
    "rm": "rm | Sets program to random mode | Syntax: rm",
    "dqb": "dqb | Displays quick buttons | Syntax: dqb",
    "thd": "thd | Start random mode with x amount of threads | Syntax: thd <numberOfThreads>",
    "setvc": "setvc | Changes voice to a specific preset | Syntax: setvc <presetName>", #presetnames == [schz, def],
    "rmq": "rmq | Says a random quote | Syntax: rmq",
    "help": "help | Prints all legal commands | Syntax: help",
    "exit": "exit | Exits current program | Syntax: exit",
}

os.system("chmod 700 ./clientsetup.sh")
livespeechclient.setupClient()

def menu():
    while True:
        if exitProgram:
            break
        printModes()
        print("> ", end="")
        mode = input() 
        checkModes(mode)

def checkModes(mode):
    try:
        print(mode)
        modeList = mode.split(" ")
        if modeList[0] == "s":
            stringToSay = ""
            for i in range(len(modeList)):
                if i == 0:
                    continue
                stringToSay = stringToSay + modeList[i] + " "
            print(stringToSay)
            speech.speak(stringToSay)
        elif modeList[0] == "help":
            printModes()
        elif modeList[0] == "exit":
            exit()
        elif modeList[0] == "cv":
            speech.changeVoice(modeList[1])
        elif modeList[0] == "rmq":
            speech.randomQuote()
        elif modeList[0] == "rm":
            speech.randomMode()
        elif modeList[0] == "vh":
            speech.getAllVoices()
        elif modeList[0] == "dqb":
            printQuickButtons()
        elif modeList[0] == "delstats":
            wordstatistics.deleteStatistics()
        elif modeList[0] == "mic": #REQUESTS MIC INPUT FROM CLIENT
            livespeechclient.startRecording()
        elif modeList[0] == "streammic": #REQUESTS MIC INPUT FROM CLIENT
            livespeechclient.streamMicrophone()
        elif modeList[0] == "thd":
            threadedspeech.startThreads(int(modeList[1]))
        elif modeList[0] == "setvc":
            if modeList[1] == "schz":
                speech.schizoPreset()
            elif modeList[1] == "def":
                speech.defaultPreset()
        elif int(modeList[0]) > -1 and int(modeList[0]) < 10:
            speech.quickWord(modeList[0])
        

    except IndexError as i:
        print(i)
    except:
        print("Error in selecting mode")

def exit():
    global exitProgram
    exitProgram = True
    print("Exiting...")

'''
-------------------------GENERAL HELPERS-------------------------
'''

def printQuickButtons():
    keysForModeList = list(speech.quickWordList.keys())
    counter = 0
    print("\n-------------------------HELP-------------------------")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(speech.quickWordList.get(key)))
    
    speech.printCurrentSelectedLanguage()

def printModes():
    keysForModeList = list(modeList.keys())
    counter = 0
    print("\n-------------------------HELP-------------------------")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(modeList.get(key)))
    
    speech.printCurrentSelectedLanguage()

'''
-------------------------MAIN PROGRAM-------------------------
'''

#printQuickButtons()
menu()