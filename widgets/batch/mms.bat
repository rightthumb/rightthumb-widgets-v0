@echo off 
python3 -c "import requests; print(str(requests.get('https://eyeformeta.com/apps/mms/').content,'iso-8859-1'))"