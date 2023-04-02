import platform
import subprocess
import random

from utils.utilsTime import UtilsTime


class UtilsShell:
    @staticmethod
    def openShell(cmd_list, workingFolder, newConsole=True):
        flag = 0
        if newConsole:
            flag |= subprocess.CREATE_NEW_CONSOLE

        sys_name = platform.system()
        if sys_name == 'Windows':
            process = subprocess.Popen(
                cmd_list,
                cwd=workingFolder,
                close_fds=True,
                creationflags=flag,
                # shell=True,
                # stdin=subprocess.PIPE,
                # stdout=subprocess.PIPE,
                # stderr=subprocess.PIPE,
            )
            return process
        else:
            raise Exception('not support')
            return None

    @staticmethod
    def poll(process):
        """
        Check if child process has terminated. Set and return returncode
        attribute.
        """
        r = subprocess.Popen.poll(process)
        return r

    @staticmethod
    def terminateShell(process):
        print('try to terminate process')
        process.terminate()
        process.kill()
        process.wait()
        return True

    @staticmethod
    def getUid():
        uid = str(UtilsTime.getTimestampNow()) + '_' + str(random.randint(0, 0x7fffffff))
        return uid



