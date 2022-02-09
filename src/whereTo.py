import fileHandling as fh
import os

pathToCurrentDir = fh.getPathToCurrentDir()

nameOfKey = "lsclientfolderkey.txt"
keyFile = pathToCurrentDir + nameOfKey

USER = "pi"
FILENAME = nameOfKey
LOCALIP = "192.168.1.144"
FILEPATH = pathToCurrentDir

def send(user, filename, ip, filepath, number):
    try:
        '''
            Number should be 0 if client is reading file
            Number should be 1 if server is reading file
        '''

        serverOrClient = ""
        if number == 0:
            serverOrClient = "server"
        elif number == 1:
            serverOrClient = "client"

        nameOfFile = pathToCurrentDir + "ls" + serverOrClient + "folderkey.txt"
        fh.removeFile(nameOfFile)
        fh.createFileInSpecifiedDir(nameOfFile)
        fh.addTextToSpecifiedFile(nameOfFile, pathToCurrentDir)
        key = pathToCurrentDir + filename
        command = "./sendfile.sh " + user + " " + key + " " + ip + " " + filepath

        #print("hei " + key)
        #print(command)
        os.system(command)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
        pass

def readFolderKey(number):

    '''
    Number should be 0 if client is reading file
    Number should be 1 if server is reading file
    '''

    serverOrClient = ""
    if number == 0:
        serverOrClient = "server"
    elif number == 1:
        serverOrClient = "client"

    split = pathToCurrentDir.split(fh.detectOS())

    homeDir = fh.detectOS() + split[1] + fh.detectOS() + split[2] + fh.detectOS()

    nameOfFile = "ls" + serverOrClient + "folderkey.txt"
    output = fh.readTXTFile(homeDir + nameOfFile)
    return output[0]