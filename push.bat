REM Use this batch file to push thid folder to github
REM Place in folder you want to upload
git init
git add .
git commit -m "New version"
git remote rm origin
git remote add origin https://github.com/szcarr/TextToSpeech.git
git pull origin main
git push -f origin main
pause