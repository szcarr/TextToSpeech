# TextToSpeech
A module that handles both text-to-speech and microphone input from client. Client comes with a text based UI.
<br>
<br>
Server will automatically setup everytime. //maybe will fix later<br>
User needs to change two variables in both livespeechclient.py and livespeechserver.py<br>
Change:<br>
USER = "<'username'>"<br>
IP = "<'ip address'>"<br>
<br>
In micsetup.py change value for nameOfMicrophone variable to match the name of the device in "arecord -l" (Does not need to be 100% accurate)
nameOfMicrophone = "<device name( in arecord -l)>"  
<br>
After all these have been set you can run:
You can then do:<br>
vlc tcp:wav//<ClientsIP>:5002 <----  in terminal on the server <br>
python3 main.py (streammic)   <----  on the client
<br>
