# TextToSpeech
A module that handles both text-to-speech and microphone input from client. Client comes with a text based UI.
<br>
Server will automatically setup everytime. //maybe will fix later
User needs to change two variables in both livespeechclient.py and livespeechserver.py
Change:
USER = "<username>"
IP = "<ip address>"
<br>
In micsetup.py change value for nameOfMicrophone to match the name of the device in "arecord -l" (Does not need to be 100% accurate)
nameOfMicrophone = "<Device name( in arecord -l)>"  
<br>
After all these have been set you can run:
You can then do:
python3 livespeechserver.py    <----  on the server
python3 livespeechclient.py    <----  on the client
<br>
