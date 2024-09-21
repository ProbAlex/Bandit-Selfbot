@echo off


:start
cls

set python_ver=311

py -3 -m pip install -r requirements.txt
cls
py -3 -m main.py

pause
exit