import ujson
import numpy

from utils.utilsFile import UtilsFile

class UtilsBuffer:
    def __init__(self, size=1000, filename='./__TEMP__'):
        self.size = size
        self.filename = filename
        self.buffers = []

        if UtilsFile.isPathExist(self.filename):
            UtilsFile.delFile(self.filename)

    def addData(self, data):
        content = ujson.dumps(data)
        self.buffers.append(content)

        if len(self.buffers) >= self.size:
            UtilsFile.appendFileLines(self.filename, self.buffers)
            self.buffers.clear()

    def close(self):
        UtilsFile.appendFileLines(self.filename, self.buffers)
        self.buffers.clear()

    def createGenerator(self, scaler):
        while True:
            with open(self.filename) as file:
                while True:
                    line = file.readline(1)
                    if line is None:
                        break

                    data = ujson.loads(line)
                    data = numpy.array(data, dtype=numpy.float32)
                    data = scaler.normalize_data(data)

                    line = file.readline(1)
                    label = ujson.loads(line)

                    yield [data, label]


