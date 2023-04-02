import lzma
import zlib
import os
import operator
import math
import time
import datetime
import gzip
import logging

from multiprocessing import Pool, cpu_count


class UtilsFile:
    @staticmethod
    def isPathExist(path):
        return os.path.exists(path)

    @staticmethod
    def delFile(path):
        return os.remove(path)

    @staticmethod
    def _copyFile(src, dst):
        open(dst, "wb").write(open(src, "rb").read())

    @staticmethod
    def copyFolder2(srcPath, dstPath):
        UtilsFile.removeFolder(dstPath)
        UtilsFile._copyFolder2(srcPath, dstPath)

    @staticmethod
    def _copyFolder2(srcPath, dstPath):
        UtilsFile.createFolder(dstPath)

        files = os.listdir(srcPath)
        for file in files:
            src_name = os.path.join(srcPath, file)
            dst_name = os.path.join(dstPath, file)
            if os.path.isfile(src_name):
                UtilsFile._copyFile(src_name, dst_name)
            else:
                os.mkdir(dst_name)
                UtilsFile._copyFolder2(src_name, dst_name)

    @staticmethod
    def createFolder(path):
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

    @staticmethod
    def removeFolder(path):
        if os.path.exists(path):
            fileList = os.listdir(path)
            for fileName in fileList:
                filePath = os.path.join(path, fileName)
                if os.path.isdir(filePath):
                    UtilsFile.removeFolder(filePath)
                else:
                    try:
                        os.remove(filePath)
                    except Exception as e:
                        print(e)

            try:
                os.rmdir(path)
            except Exception as e:
                print(e)

    @staticmethod
    def readFileContent(filename, encoding=None):
        lines = UtilsFile.readFileLines(filename, encoding)
        content = ''
        for line in lines:
            content += line
        return content

    @staticmethod
    def writeFileLines(filename, lines, encoding=None):
        with open(filename, 'w', encoding=encoding) as file:
            file.writelines(lines)
            file.close()

    @staticmethod
    def appendFileLines(filename, lines, encoding=None):
        with open(filename, 'a', encoding=encoding) as file:
            file.writelines(lines)
            file.close()

    @staticmethod
    def writeFileLinesSafety(filename, lines, encoding=None):
        while True:
            try:
                _filename = filename + '.temp'
                UtilsFile.writeFileLines(_filename, lines, encoding)

                if os.path.exists(filename):
                    os.remove(filename)
                os.rename(_filename, filename)
                return True

            except Exception as e:
                print('\t', 'fail to save file', filename, e, '\n')
                return False

    @staticmethod
    def readFileBinary(filename):
        with open(filename, mode='rb') as file:
            bin = file.read()
            file.close()
            return bin

    @staticmethod
    def writeFileBinary(filename, bin):
        with open(filename, 'wb') as file:
            file.write(bin)
            file.close()

    @staticmethod
    def readFileLines(filename, encoding=None):
        with open(filename, encoding=encoding) as file:
            lines = file.readlines()
            file.close()
            return lines
        return []

    @staticmethod
    def writeLzmaFileLines(filename, lines):
        s = ''
        for line in lines:
            s += line
        b = s.encode()

        with lzma.open(filename, 'w') as file:
            file.write(b)
            file.close()

    @staticmethod
    def readLzmaFileLines(filename):
        with lzma.open(filename) as file:
            b = file.read()
            file.close()

            s = b.decode()
            lines = s.split('\n')
            return lines

        return []

    @staticmethod
    def writeZipFileLines(filename, lines):
        s = ''
        for line in lines:
            s += line
        b = s.encode()
        c = zlib.compress(b, zlib.Z_BEST_SPEED)

        with open(filename, 'wb') as file:
            file.write(c)
            file.close()

    @staticmethod
    def readZipFileLines(filename):
        with open(filename, 'rb') as file:
            c = file.read()
            b = zlib.decompress(c)
            s = b.decode()
            lines = s.split('\n')
            return lines

        return []

    @staticmethod
    def readGZipFileLines(filename):
        with open(filename, 'rb') as file:
            c = file.read()
            b = gzip.decompress(c)
            s = b.decode()
            lines = s.split('\n')
            return lines

        return []

    @staticmethod
    def readGZipFileLinesGenerator(filename, bufferSize=256*1024*1024):
        buffer = ''

        fin = gzip.open(filename, 'rb')
        while True:
            bin = fin.read(bufferSize)
            if len(bin) < 1:
                fin.close()
                if buffer != '':
                    yield [buffer]
                break

            s = bin.decode()
            buffer += s

            splits = buffer.split('\n')
            buffer = splits[-1]
            splits.pop(-1)

            yield splits

    @staticmethod
    def readGZipFileLinesStreamly(filename, bufferSize=256*1024*1024):
        lines = []
        buffer = ''

        fin = gzip.open(filename, 'rb')
        while True:
            bin = fin.read(bufferSize)
            if len(bin) < 1:
                fin.close()
                if buffer != '':
                    lines.append(buffer)
                break

            s = bin.decode()
            buffer += s

            splits = buffer.split('\n')
            buffer = splits[-1]
            splits.pop(-1)

            for i in range(len(splits)):
                lines.append(splits[i])

        return lines

    @staticmethod
    def gzip_compress_file(source, destination):
        if UtilsFile.isPathExist(source):
            b = UtilsFile.readFileBinary(source)
            try:
                f = gzip.open(destination, mode='wb')
                f.write(b)
                f.close()
            except Exception as e:
                print('fail to save file', destination)
                print(e)
        else:
            print('file not exist', source)

    @staticmethod
    def merge_text_files(source_list: list, destination):
        with open(destination, 'wt') as outfile:
            for source in source_list:
                with open(source, 'rt') as infile:
                    outfile.write(infile.read())


