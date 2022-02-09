import threading
import speech

def startThreads(amountOfThreads):
    threads = []

    for i in range(amountOfThreads):
        t = threading.Thread(target=speech.randomMode, args=())
        t.daemon = True
        threads.append(t)

    for i in range(amountOfThreads):
        threads[i].start()

    for i in range(amountOfThreads):
        threads[i].join()