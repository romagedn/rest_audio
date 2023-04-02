import lzma
import zlib
import os
import operator
import math
import time
import datetime
import gzip
import logging

from threading import Timer


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)



