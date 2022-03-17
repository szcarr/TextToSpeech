import os
import time
import keyboard

import fileHandling as fh
import whereTo as w
import micsetup

pathToCurrentDir = fh.getPathToCurrentDir() 

audioFile = "micaudio.wav" #DONT CHANGE 
keyFile = pathToCurrentDir + "key.txt"
#speaker-test -t sine -f 1000 -l 110

USER = "isak" #CHANGE THIS TO MATCH USER NAME TO WHERE THE SERVER IS
IP = "192.168.1.131" #CHANGE THIS TO MATCH THE IP OF WHERE THE SERVER IS

ESTABLISHFILE = "lsclientfolderkey.txt" #DO NOT CHNGE

WHERETOSENDESTABLISH = "/home/" + USER + "/" #DO NOT CHANGE

FILENAME = audioFile
WHERETOSENDAUDIOFILE = None

wheretosendaudiohasbeenfound = False
doExit = False

def setupClient():
    os.system("./clientsetup.sh")

def streamMicrophone():
    audiocard, devicecard = micsetup.main()
    #os.system("ffmpeg -ar 44100 -ac 1 -f alsa -i plughw:" + "1,0" + " -f wav -listen 1 tcp://0.0.0.0:5002")
    os.system("ffmpeg -ar 44100 -ac 1 -f alsa -i plughw:" + audiocard + "," + devicecard + " -f wav -listen 1 tcp://0.0.0.0:5002")