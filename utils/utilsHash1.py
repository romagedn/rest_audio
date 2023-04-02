
import hashlib

class UtilsHash:
    @staticmethod
    def calc_data_md5(str):
        md5hash = hashlib.md5(str)
        md5 = md5hash.hexdigest()
        return md5


    @staticmethod
    def calc_file_md5(filename):
        try:
            with open(filename, 'rb') as fp:
                data = fp.read()
            file_md5 = hashlib.md5(data).hexdigest()
            return file_md5

        except:
            return None

