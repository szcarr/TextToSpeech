import os

def generateRandomQuote():
    quote = str(os.popen("fortune -a").read())
    return quote

