start .\venv\Scripts\python main.py

echo start repeating worker
echo off

:_BEGIN_

call .\venv\Scripts\python worker.py

goto _BEGIN_

pause