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

def main():
    os.system("cd ~ & cvlc tcp:wav//" + IP + ":5002") #"cvlc tcp://" + IP + ":5002"  "vlc tcp://" + IP + ":5002"

main()