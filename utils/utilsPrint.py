import json


class UtilsPrint:
    @staticmethod
    def printDict(d:dict, indent=4, ensure_ascii=True):
        print(json.dumps(d, indent=indent, ensure_ascii=ensure_ascii))

    @staticmethod
    def pretty_print_dict(d: dict, indent: int = 0) -> None:
        """
        以结构化的方式输出字典的内容。

        :param d: 要输出的字典。
        :param indent: 输出时每一层的缩进量，默认为0。
        :return: 无返回值，直接将输出打印到控制台。
        """
        for key, value in d.items():
            # 根据缩进量输出空格
            print(" " * indent, end="")

            # 如果值是字典，则递归调用pretty_print_dict()函数
            if isinstance(value, dict):
                print(f"{key}:")
                UtilsPrint.pretty_print_dict(value, indent + 2)
            else:
                print(f"{key}: {value}")

    @staticmethod
    def printKeys(dataKeys, split=', ', width=150, output=True):
        SPLIT = split
        WIDTH = width

        s = 'keys count = {}\n'.format(len(dataKeys))

        line = ''
        for key in dataKeys:
            if len(line + str(key) + SPLIT) > WIDTH:
                s += line + '\n'
                line = ''
            line += str(key) + SPLIT

        s += line + '\n'
        s += '\n'
        if output:
            print(s)
        return s

