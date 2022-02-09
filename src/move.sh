#Ikkje tenk paa denne
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ..
cd ..

#USER="isak"
#IP="192.168.1.131"
USER="pi"
IP="192.168.1.144"

rm -rf TextToSpeech.zip
zip -r TextToSpeech.zip TextToSpeech
scp TextToSpeech.zip $USER@$IP:/home/$USER/
rm -rf TextToSpeech.zip