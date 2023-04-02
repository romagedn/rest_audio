

class ResponseHelper:
    @staticmethod
    def generateResponse(status, fields:dict=None):
        if fields is None:
            fields = {}
        info = {
            'status': status,
        }
        info.update(fields)
        return info

