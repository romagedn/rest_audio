echo start repeating worker
echo off

start .\venv\Scripts\python main.py

:_BEGIN_

.\venv\Scripts\python worker.py

goto _BEGIN_

