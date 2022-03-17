import os

import fileHandling as fh
import livespeechclient

def main():
    nameOfMicrophone = "USB Audio"

    cardNumber = -1
    deviceNumber = -1

    print("Setting up microphone.")
    foundMicrophone = False
    try:
        allOutput = str(os.popen("arecord -l").read()).split("\n")
        for i in range(len(allOutput)):
            line = allOutput[i]
            if nameOfMicrophone in line:
                foundMicrophone = True
                print("Found device name.")
                splitList = line.split(" ")
                for x in range(len(splitList)):
                    output = splitList[x]
                    if output == "card":
                        cardNumber = splitList[x + 1].split(":")[0]
                        print("Card: " + cardNumber)
                    elif output == "device":
                        deviceNumber = splitList[x + 1].split(":")[0]
                        print("Device: " + deviceNumber)
        if foundMicrophone == False:
            print("Did not find " + nameOfMicrophone + " in arecord -l. Check if nameOfMicrophone variable is set to the correct name. Find correct name by: arecord -l find device name. Then change value of variable to name of Audio device.")

    except:
        pass

    '''
            output = str(os.popen("arecord -l | head -2 | tail -1 | awk -F' ' '{print $2}' | awk -F':' '{print $1}'").read())
            if output == "card":
                cardNumber = output
            elif output == "device":
                deviceNumber = output
    '''

    failedRetrievingValues = False
    if deviceNumber == -1 or cardNumber == -1:
        failedRetrievingValues = True

    if failedRetrievingValues == False: #IF FALSE ALL GOOD
        soundFile = "/home/pi/.asoundrc"

        stringToEnterToFile = '''
    pcm.!default {
    type asym
    capture.pcm "mic"
    }
    pcm.mic {
    type plug
    slave {
        pcm "hw:''' + cardNumber + ''',''' + deviceNumber + '''"
    }
    }
        '''

        try:
            fh.removeFile(soundFile)
            fh.createFileInSpecifiedDir(soundFile)
            fh.addTextToSpecifiedFile(soundFile, stringToEnterToFile)
            print("Added " + nameOfMicrophone + " to " + soundFile)
        except:
            pass
        return cardNumber, deviceNumber

main()