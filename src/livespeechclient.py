import os
import time
import keyboard

import fileHandling as fh
import whereTo as w

pathToCurrentDir = fh.getPathToCurrentDir() 

audioFile = "micaudio.wav" #DONT CHANGE 
keyFile = pathToCurrentDir + "key.txt"
#speaker-test -t sine -f 1000 -l 110

USER = "scp092" #CHANGE THIS TO MATCH USER NAME TO WHERE THE SERVER IS
IP = "192.168.1.103" #CHANGE THIS TO MATCH THE IP OF WHERE THE SERVER IS

ESTABLISHFILE = "lsclientfolderkey.txt" #DO NOT CHNGE

WHERETOSENDESTABLISH = "/home/" + USER + "/" #DO NOT CHANGE

FILENAME = audioFile
WHERETOSENDAUDIOFILE = None

wheretosendaudiohasbeenfound = False
doExit = False

def setupClient():
    os.system("./clientsetup.sh " + USER + " " + IP)

def startRecording(*args):
    global doExit
    if args:
        durationOfMicInput = args[0]
    else:
        WHERETOSENDAUDIOFILE = initialize()
    durationOfMicInput = 5
    try:
        print("Starting recording. Press 'ctrl+c' to abort. Microphone automatically aborts after " + str(durationOfMicInput) + " seconds")
        os.popen("chmod 777 recordmic.sh")
        os.popen("sh recordmic.sh " + str(durationOfMicInput)) #arecord -f cd micaudio.wav | tee micaudio.wav | aplay -
        time.sleep(durationOfMicInput)
    except OSError as e:
        print(e)
    except KeyboardInterrupt as e:
        doExit = True
        print(e)
    finally:
        print("Attempting to send audio file.")
        sendFile()

def listen():
    #MAIN
    #OLD
    initialize()
    try:
        fh.removeFile(keyFile)
        counter = 0
        while True:
            counter = counter + 1
            if counter % 7 == 0:
                w.send(USER, ESTABLISHFILE, IP, WHERETOSENDESTABLISH, 1)
            if counter > 25000050050:
                counter = 0
            if fh.checkIfFileExist(keyFile):
                print("Detected key.")
                startRecording()
                fh.removeFile(keyFile)
            time.sleep(1)
    except OSError as e:
        print(e)
    except KeyboardInterrupt:
        print("Exiting from main.")
        pass

def sendFile():

    '''
    target is
    <username@ip:dir>
    example:
    isak@192.168.1.131:/home/isak/
    '''
    #print("scp " + FILENAME + " " + USER + "@" + IP + ":" + WHERETOSENDAUDIOFILE)
    os.system("./sendfile.sh " + USER + " " + FILENAME + " " + IP + " " + WHERETOSENDAUDIOFILE)

def initialize():
    global WHERETOSENDAUDIOFILE
    print("Sending " + ESTABLISHFILE + " to " + USER + "@" + IP + ":" + WHERETOSENDESTABLISH)
    w.send(USER, ESTABLISHFILE, IP, WHERETOSENDESTABLISH, 1)
    split = pathToCurrentDir.split(fh.detectOS())
    homeDir = fh.detectOS() + split[1] + fh.detectOS() + split[2] + fh.detectOS()
    print("Waiting for confirmed handshake.")
    try:
        while True: #WAITING FOR HANDSHAKE   
            if fh.checkIfFileExist(homeDir + "lsserverfolderkey.txt"):
                print("Successfully handshaken with " + USER + "@" + IP)
                WHERETOSENDAUDIOFILE = w.readFolderKey(0)
                fh.removeFile(homeDir + "lsserverfolderkey.txt")
                return WHERETOSENDAUDIOFILE
            time.sleep(1)
    except Exception as e:
        print(e)

def streamMicrophone():
    initialize()
    try:
        while True:
            if doExit:
                break
            time.sleep(0.1)
            startRecording(2)
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)