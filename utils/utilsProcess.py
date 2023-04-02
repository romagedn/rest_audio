from multiprocessing import Pool, cpu_count


class UtilsProcess:
    _shareProcessPoolMap = {}
    _shareProcessPoolCount = None

    @staticmethod
    def getShareProcessCount():
        return int(cpu_count())

    @staticmethod
    def shareProcessPool(_maxProcessCount=None):
        maxProcessCount = UtilsProcess.getShareProcessCount() - 1
        if _maxProcessCount:
            maxProcessCount = min(maxProcessCount, _maxProcessCount)

        if maxProcessCount not in UtilsProcess._shareProcessPoolMap:
            UtilsProcess._shareProcessPoolMap[maxProcessCount] = Pool(maxProcessCount)

        return UtilsProcess._shareProcessPoolMap[maxProcessCount], maxProcessCount

    @staticmethod
    def queryProcessPool(maxProcessCount=None):
        if maxProcessCount:
            n = min(maxProcessCount, UtilsProcess.getShareProcessCount())
        else:
            n = UtilsProcess.getShareProcessCount()
        pool = Pool(UtilsProcess._shareProcessPoolCount)
        return pool, n
