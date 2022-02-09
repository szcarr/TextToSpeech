import os
import time

import fileHandling as fh
import whereTo as w

#whereToSendKeyFileTo = "pi@192.168.1.144:/home/pi/"
pathToCurrentDir = fh.getPathToCurrentDir()

audioFile = "micaudio.wav" 
nameOfKey = "key.txt"
keyFile = pathToCurrentDir + nameOfKey #KEY IS USED TO REQUEST MIC INPUT

USER = "pi" #<------------------------------------ må endre her
IP = "192.168.1.175" #<------------------------------------ må endre her
FILEPATH = pathToCurrentDir

ESTABLISHFILE = "lsserverfolderkey.txt" #DO NOT CHANGE

WHERETOSENDESTABLISH = "/home/" + USER + "/" #DO NOT CHANGE

WHERETOSENDKEYFILES = ""

def setupServer():
    os.system("./serversetup.sh " + USER + " " + IP)

def requestRecording():
    #MAIN
    #OLD
    setupServer()
    initialize()
    print("Requesting microphone input.")
    fh.removeFile(pathToCurrentDir + audioFile)
    fh.createFileInSpecifiedDir(keyFile)
    command = "./sendfile.sh " + USER + " " + keyFile + " " + IP + " " + WHERETOSENDKEYFILES # SENDING KEY HERE
    print(command)
    os.popen(command)
    listen()

def listen(): #check if voice file exist 
    #MAIN
    setupServer()
    initialize()
    try:
        split = pathToCurrentDir.split(fh.detectOS())
        homeDir = fh.detectOS() + split[1] + fh.detectOS() + split[2] + fh.detectOS()
        while True:
            if fh.checkIfFileExist(pathToCurrentDir + audioFile):
                os.system("aplay " + audioFile)
                print("Ferdig å spele av lyd.")
                fh.removeFile(pathToCurrentDir + audioFile)
            elif fh.checkIfFileExist(homeDir + "lsclientfolderkey.txt"):
                print("Successfully handshaken with " + USER + "@" + IP)
                WHERETOSENDKEYFILES = w.readFolderKey(1)
                w.send(USER, ESTABLISHFILE, IP, WHERETOSENDESTABLISH, 0)
                fh.removeFile(homeDir + "lsclientfolderkey.txt")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    except OSError as e:
        print(e)

def ping():
    pass

def initialize():

    global WHERETOSENDKEYFILES
    print("Sending " + ESTABLISHFILE + " to " + USER + "@" + IP + ":" + WHERETOSENDESTABLISH)

    w.send(USER, ESTABLISHFILE, IP, WHERETOSENDESTABLISH, 0)

    split = pathToCurrentDir.split(fh.detectOS())
    homeDir = fh.detectOS() + split[1] + fh.detectOS() + split[2] + fh.detectOS()

    print("Waiting for confirmed handshake")
    while True: #WAITING FOR HANDSHAKE
        time.sleep(1)
        if fh.checkIfFileExist(homeDir + "lsclientfolderkey.txt"):
            print("Successfully handshaken with " + USER + "@" + IP)
            WHERETOSENDKEYFILES = w.readFolderKey(1)
            fh.removeFile(homeDir + "lsclientfolderkey.txt")
            break
    print("Sending to: " + WHERETOSENDKEYFILES)

listen()