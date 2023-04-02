import re


class UtilsString():
    @staticmethod
    def replace(string_str, tokenMap):
        for t in tokenMap:
            s = str(tokenMap[t])
            k = '{' + t + '}'
            string_str = string_str.replace(k, s)
        return string_str

    @staticmethod
    def len_zh(s: str):
        l = len(s)
        l8 = len(s.encode('utf-8'))
        n = int((l8 - l) / 2 + l)
        return n

    @staticmethod
    def rjust(s, n):
        l = UtilsString.len_zh(s)
        c = n - l
        if c > 0:
            s = s + ' ' * c
        return s

    @staticmethod
    def ljust(s, n):
        l = UtilsString.len_zh(s)
        c = n - l
        if c > 0:
            s = ' ' * c + s
        return s

