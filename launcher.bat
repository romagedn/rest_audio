start .\venv\Scripts\python main.py

echo start repeating worker
echo off

:_BEGIN_

.\venv\Scripts\python worker.py

goto _BEGIN_

