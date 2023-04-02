


class UtilsReport:
    def __init__(self, name):
        self.name = name
        self.logs = []

    def add(self, *logs):
        print(*logs)

        line = ''
        for log in logs:
            line += str(log) + '\t'
        line += '\n'
        self.logs.append(line)

    def save(self):
        UtilsReport.writeFileLines(self.name, self.logs)

    @staticmethod
    def writeFileLines(filename, lines):
        with open(filename, 'w') as file:
            file.writelines(lines)
            file.close()

    @staticmethod
    def appendFileLines(filename, lines):
        with open(filename, 'a') as file:
            file.writelines(lines)
            file.close()
