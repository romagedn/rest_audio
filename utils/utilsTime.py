import lzma
import zlib
import os
import operator
import math
import time
import datetime
import gzip
import logging


class UtilsTime:
    @staticmethod
    def getTimestamp(datetimeStr, format='%Y-%m-%d %H:%M:%S'):
        timeArray = time.strptime(datetimeStr, format)
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    @staticmethod
    def getDatetimeStr(timestampSec, format='%Y-%m-%d %H:%M:%S'):
        timeArray = time.localtime(timestampSec)
        date = time.strftime(format, timeArray)
        return date

    @staticmethod
    def getDatetimeFromTimeStamp(timestampSec):
        date = datetime.datetime.fromtimestamp(timestampSec)
        return date

    @staticmethod
    def getDatetimeStrNow(format='%Y-%m-%d %H:%M:%S'):
        a = datetime.datetime.now()
        b = a.strftime(format)
        return b

    @staticmethod
    def getTimestampNow(toInteger=True):
        a = time.time()
        if toInteger:
            a = int(a)
        return a

    @staticmethod
    def formatSeconds(sec):
        if math.isinf(sec) or sec > 24 * 3600 * 365:
            sec = 24 * 3600 * 365

        d = int(sec / 60 / 60 / 24)
        sec -= d * 60 * 60 * 24
        h = int(sec / 60 / 60)
        sec -= h * 60 * 60
        m = int(sec / 60)
        sec = int(sec - m * 60)
        return str(d) + 'd-' + str(h) + 'h-' + str(m) + 'm-' + str(sec) + 's'
