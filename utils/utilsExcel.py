import csv

from io import StringIO


class UtilsExcel:
    @staticmethod
    def readCsv(filename):
        titles = None
        lines = []
        with open(filename, 'r') as myFile:
            reader = csv.reader(myFile)
            for line in reader:
                if titles is None:
                    titles = [c.encode('gbk').decode('utf8') for c in line]

                    if titles[0].startswith(u'\ufeff'):
                        titles[0] = titles[0].encode('utf8')[3:].decode('utf8')

                else:
                    lines.append((line))
            return titles, lines

    @staticmethod
    def readCsvFromStream(bin):
        titles = None
        lines = []
        reader = csv.reader(StringIO(bin.decode('utf-8'), newline=''))
        for line in reader:
            if titles is None:
                titles = line

                if titles[0].startswith(u'\ufeff'):
                    titles[0] = titles[0].encode('utf8')[3:].decode('utf8')

            else:
                lines.append((line))
        return titles, lines



