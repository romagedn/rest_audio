import base64


class UtilsEncode:
    @staticmethod
    def base64_encode(s:str):
        a = s.encode()
        a = base64.encodebytes(a)
        a = a.decode()
        return a

    @staticmethod
    def base64_decode(s:str):
        try:
            a = s.encode()
            a = base64.decodebytes(a)
            a = a.decode()
            return a
        except:
            return s


