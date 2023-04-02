import math
import random


class UtilsMath:
    @staticmethod
    def isInteger(v):
        try:
            a = int(v)
            return a == v
        except Exception as e:
            return False

    @staticmethod
    def isNumber(v):
        try:
            a = float(v)
            return True
        except Exception as e:
            return False

    @staticmethod
    def _normalizeAtan(x):
        return math.atan(x) * 2 / math.pi

    @staticmethod
    def clip(v, a, b):
        return min(max(v, a), b)

    @staticmethod
    def intToBinaryArray(din, bit_width):
        """
        Parameters
        ----------
        din : int/float
            input data
        bit_width : int
            bit width of binary array need to convert to

        Returns
        -------
        int array, each element is the binary bit of din
        o_arr[0] correspond to din bit 0

        """
        bin_obj = bin(int(din))[2:]
        bin_str = bin_obj.rjust(bit_width, '0')
        o_arr = []
        for ii in range(len(bin_str)):
            o_arr.append(int(bin_str[len(bin_str) - ii - 1]))
        return o_arr

    @staticmethod
    def getWeightedRandomIndexList(weights, count):
        index = []
        for i in range(count):
            r = [math.pow(random.random(), 1 / (abs(w) + 1e-6)) for w in weights]
            index.append(r[0])
        return index


if __name__ == '__main__':
    ca = 3
    ba = UtilsMath.intToBinaryArray(ca, 6)
    print(ba)

