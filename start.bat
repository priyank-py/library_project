@echo off
cmd /k "C: /d virtualenv testenv & cd .\testenv\Scripts & activate & ../.. & pip install -r requirements.txt & python manage.py migrate & python manage.py runserver"