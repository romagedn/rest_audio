import base64
import json
import logging
import sys
from io import BytesIO

import tornado.gen
import tornado.web
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

from utils.responseHelper import ResponseHelper
from utils.utilsFile import UtilsFile
from utils.utilshash import UtilsHash


class Handler_updateAudio(tornado.web.RequestHandler):
    initialized = False


    @tornado.gen.coroutine
    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.finish('copy')

    @tornado.gen.coroutine
    def post(self):
        self.dispose()


    def dispose(self):
        try:
            body = self.request.body
            content = json.loads(body)
            image64 = content['image64']

            bytes_image = base64.standard_b64decode(image64)
            hash = UtilsHash.calc_data_md5(bytes_image)

            filename = './temp/{}.png'.format(hash)
            UtilsFile.writeFileBinary(filename, bytes_image)

            url = self.upload(filename, hash)

            response = ResponseHelper.generateResponse(True)
            response['storage_url'] = url

            self.write(json.dumps(response))
            self.finish()

        except Exception as e:
            print('server internal error')
            logging.exception(e)

            self.set_header("Content-Type", "text/plain")
            response = ResponseHelper.generateResponse(False)
            self.write(json.dumps(response))
            self.finish()


    def loadConfig(self):
        if Handler_updateAudio.initialized:
            return

        filename = './config.txt'

        content = UtilsFile.readFileContent(filename)
        content = json.loads(content)

        Handler_updateAudio.secret_id = content['secret_id']
        Handler_updateAudio.secret_key = content['secret_key']
        Handler_updateAudio.region = content['region']
        Handler_updateAudio.Bucket = content['Bucket']
        Handler_updateAudio.initialized = True


    def upload(self, filename, md5):
        self.loadConfig()
        if not Handler_updateAudio.initialized:
            return ''

        # 正常情况日志级别使用 INFO，需要定位时可以修改为 DEBUG，此时 SDK 会打印和服务端的通信信息
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)

        # 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
        secret_id = Handler_updateAudio.secret_id  # 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
        secret_key = Handler_updateAudio.secret_key  # 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
        region = Handler_updateAudio.region  # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
        # COS 支持的所有 region 列表参见 https://cloud.tencent.com/document/product/436/6224
        token = None  # 如果使用永久密钥不需要填入 token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
        scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

        config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
        client = CosS3Client(config)


        #### 文件流简单上传（不支持超过5G的文件，推荐使用下方高级上传接口）
        # 强烈建议您以二进制模式(binary mode)打开文件,否则可能会导致错误
        # filename = 'face.png'

        # md5 = UtilsHash.calc_file_md5(filename)

        if md5:
            key = 'img_' + md5 + '.png'

            with open(filename, 'rb') as fp:
                response = client.put_object(
                    Bucket=Handler_updateAudio.Bucket,
                    Body=fp,
                    Key=key,
                    StorageClass='STANDARD',
                    EnableMD5=False,
                )
            # print(response)
            print(response['ETag'])

            url = 'https://{}.cos.ap-beijing.myqcloud.com/{}.png'.format(self.Bucket, key)
            print(url)
            return url





