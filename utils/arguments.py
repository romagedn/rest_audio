import sys


class Arguments:
    def __init__(self, log=True):
        self.log = log

    def getArgument(self, field, default):
        n = len(sys.argv)
        for i in range(1, n):
            arg = str(sys.argv[i])
            pair = arg.split('=', maxsplit=1)
            if len(pair) < 2:
                continue

            k = pair[0]
            v = pair[1]

            if k == field:
                if self.log:
                    print(field, '=', v)
                return v

        if self.log:
            print(field, '=', default)
        return default

    @staticmethod
    def getCommandLine():
        line = []
        for a in sys.argv:
            line.append(a)
        return '\n'.join(line)



