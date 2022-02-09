import fileHandling as fh

statsFile = fh.getPathToCurrentDir() + "statistics.txt"

def addStatistics(word):
    try:
        fh.createFileInSpecifiedDir(statsFile)
    except OSError as o:
        print(o)

    if fh.fileContainsString(statsFile, word): #found word in file
        contentOfFile = fh.readTXTFile(statsFile)
        for i in range(len(contentOfFile)):
            splitList = contentOfFile[i]
            if splitList[0] == word:
                newNumber = int(splitList[i]) + 1
                fh.replaceLineInFile(statsFile, i, word + " " + newNumber)
                break
    else: #Word not found in file
        fh.addTextToSpecifiedFile(statsFile, word + " " + str(1) + "\n")

def deleteStatistics():
    try:
        fh.removeFile(statsFile)
    except OSError as o:
        print(o)
        