
import requests
import json
import base64
import random

from utils.utilsTime import UtilsTime


filename = './data/cn.wav'


with open(filename, 'rb') as fp:
    uid = str(UtilsTime.getTimestampNow()) + '_' + str(random.randint(0, 0x7fffffff))
    print('uid', uid)

    img = fp.read()
    img64 = base64.standard_b64encode(img).decode()
    img_ = base64.standard_b64decode(img64)

    msg = '目标音频的内容文本列表，目前只支持中文，不支持添加标点符号。'

    data = json.dumps({
        'audio': img64,
        'message': msg,
        'uid': uid,
    })

    header = {
        "Content-Type": "text/plain",
    }
    response = requests.post(url='http://localhost:13132/upload', data=data, headers=header)
    print(response.content)

