import requests
import json


class DingDingHelper:
    url_ai = 'https://oapi.dingtalk.com/robot/send?access_token=9cbd3d574e1de03ff68ccec6d6a1d1f66ea02aa4e7f3f6ffbc2d24a7c92048ce'
    active_post = True

    @staticmethod
    def post(webhook, msg):
        if not DingDingHelper.active_post:
            return None

        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        message = {
            "msgtype": "text",
            "text": {
                "content": '_AI_' + msg
            },
            # "at": {
            #     "isAtAll": True
            # }

        }

        message_json = json.dumps(message)
        try:
            info = requests.post(url=webhook, data=message_json, headers=header)
            return info
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    DingDingHelper.post(DingDingHelper.url_ai, 'test')


