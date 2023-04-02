from utils.utilsList import UtilsList


class UtilsDict:
    @staticmethod
    def sortKeyValueMap(kvMap, reverse=False, count=10):
        elements = [{'k': k, 'v': kvMap[k]} for k in kvMap]
        elements = UtilsList.sortDictContents(elements, 'v', reverse, count)
        kvMap = {e['k']: e['v'] for e in elements}
        return kvMap

    @staticmethod
    def sorkMap(dest:dict, key, reverse=False, count=10, cbWeight=None):
        keys = list(dest.keys())
        values = list(dest.values())
        if cbWeight:
            elements = [{
                'k': keys[i],
                'v': cbWeight(values[i][key])
            } for i in range(len(dest))]
        else:
            elements = [{
                'k': keys[i],
                'v': values[i][key]
            } for i in range(len(dest))]
        elements = UtilsList.sortDictContents(elements, 'v', reverse, count)
        dest = {
            e['k']: dest[e['k']] for e in elements
        }
        return dest

    @staticmethod
    def consisitIntoSortMap(elements: list, reverse=False):
        kvMap = {i: elements[i] for i in range(len(elements))}
        kvMap = UtilsDict.sortKeyValueMap(kvMap, reverse, 0)
        return kvMap


