import subprocess
import time

from utils.utilsShell import UtilsShell
from http.client import HTTPConnection
from utils.utilsTime import UtilsTime
from utils.utilsFile import UtilsFile
from utils.utilsTimer import RepeatingTimer
from utils.arguments import Arguments


class ShellGuard:
    CLIENT_LIFECYCLE = 60 * 60
    CLIENT_TIMEOUT = 10 * 60

    def __init__(self, cmd, workingPath):
        self.cmd = cmd
        self.workingPath = workingPath

    def start(self):
        while True:
            print('starting a new task')
            process = subprocess.Popen(self.cmd, cwd=self.workingPath, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())

            rc = process.poll()
            print('finish one task, return code', rc)
            print('\n')
            time.sleep(0.01)


if __name__ == '__main__':
    argument = Arguments()
    CMD = argument.getArgument('CMD', '.\\venv\\Scripts\\activate.bat && python worker.py')
    WORKING_PATH = argument.getArgument('WORKING_PATH', './')

    print('parameter:')
    print('CMD', CMD)
    print('WORKING_PATH', WORKING_PATH)
    print('')

    guard = ShellGuard(CMD, WORKING_PATH)
    guard.start()

