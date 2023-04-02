import random


class UtilsList:

    '''
    sort list contents contained in dict
    '''
    @staticmethod
    def sortDictContents(elements: list, key: str, reverse=False, count=10, cbWeight=None):
        elements = elements.copy()
        if cbWeight:
            elements.sort(key=lambda e: cbWeight(e[key]), reverse=reverse)
        else:
            elements.sort(key=lambda e: e[key], reverse=reverse)

        if count > 0:
            elements = elements[:count]
        return elements

    @staticmethod
    def deleteFromList(set:list, indexSet:list):
        _set = []
        _delete_set = []
        for i in range(len(set)):
            if i not in indexSet:
                _set.append(set[i])
            else:
                _delete_set.append(set[i])
        return _set, _delete_set

    @staticmethod
    def createRandomIndex(n):
        a = list(range(n))
        random.shuffle(a)
        return a

    @staticmethod
    def randomPickup(elements):
        n = len(elements)
        index = random.randint(0, n - 1)
        return elements[index]

    @staticmethod
    def getTopAt(array, position, reverse):
        _array = list(array)
        _array.sort(reverse=reverse)
        position = min(position, len(array) - 1)
        e = _array[position]
        return e

    @staticmethod
    def getMiddleOf(array):
        position = int(len(array) / 2)
        return UtilsList.getTopAt(array, position, False)

    @staticmethod
    def findDuplicateCount(src: list, dest: list, toRate: bool = True) -> float:
        """
        计算两个列表中重复元素的数量，并可以将结果归一化为一个比例。

        :param src: 包含一些元素的列表。
        :param dest: 包含一些元素的列表。
        :param toRate: 一个布尔值，指示是否将计数结果转换为比例。
        :return: 重复元素的数量，如果toRate为True，则返回重复元素数量与src长度的比率，否则返回重复元素数量。
        """
        # 计算两个列表中重复元素的数量
        count = len(src) + len(dest) - len(set(src + dest))

        # 如果toRate为True，则将计数结果转换为比例
        if toRate:
            count /= max(len(src), 1e-6)  # 避免除以零的问题

        # 返回重复元素的数量或比例
        return count
