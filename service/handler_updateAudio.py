import base64
import json
import logging
import os
import tornado.gen
import tornado.web

from utils.responseHelper import ResponseHelper
from utils.utilsFile import UtilsFile

from worker import task_folder, output_folder

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
            audio64 = content['audio']
            message = content['message']
            uid = content['uid']

            wavs_base64, speech_texts = self.check_output(uid)
            if wavs_base64 and speech_texts:
                # is done
                response = ResponseHelper.generateResponse(True)
                response['complete'] = 1
                response['speech_wavs'] = wavs_base64
                response['speech_texts'] = speech_texts

                self.write(json.dumps(response))
                self.finish()
                return

            if self.check_task(uid):
                response = ResponseHelper.generateResponse(True)
                response['complete'] = 0

                self.write(json.dumps(response))
                self.finish()
                return

            # create a new task
            bytes_audio = base64.standard_b64decode(audio64)

            audio_filename = task_folder + uid + '.wav'
            UtilsFile.writeFileBinary(audio_filename, bytes_audio)

            des = {
                'sample_file': os.path.basename(audio_filename),
                'message': message,
            }
            des_filename = task_folder + uid + '.txt'
            UtilsFile.writeFileLines(des_filename, [json.dumps(des)])

            response = ResponseHelper.generateResponse(True)
            response['complete'] = 0

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

        #
        Handler_updateAudio.initialized = True


    def clear_output(self, uid):
        try:
            des_filename = output_folder + uid + '.txt'
            if UtilsFile.isPathExist(des_filename):
                content = UtilsFile.readFileContent(des_filename)
                cfg = json.loads(content)
                speech_wavs = cfg['speech_wavs']
                speech_texts = cfg['speech_texts']

                for wav in speech_wavs:
                    wav_filename = output_folder + wav
                    if UtilsFile.isPathExist(wav_filename):
                        UtilsFile.delFile(wav_filename)

                UtilsFile.delFile(des_filename)
                print('delete output, uid = ', uid)
        except:
            pass


    def check_output(self, uid):
        des_filename = output_folder + uid + '.txt'
        if UtilsFile.isPathExist(des_filename):
            try:
                content = UtilsFile.readFileContent(des_filename)
                cfg = json.loads(content)
                speech_wavs = cfg['speech_wavs']
                speech_texts = cfg['speech_texts']

                wavs_base64 = []
                for wav in speech_wavs:
                    wav_filename = output_folder + wav
                    if UtilsFile.isPathExist(wav_filename):
                        bin = UtilsFile.readFileBinary(wav_filename)
                        b64 = base64.standard_b64encode(bin).decode()
                        wavs_base64.append(b64)

                return wavs_base64, speech_texts

            except:
                self.clear_output(uid)

        return None, None


    def check_task(self, uid):
        des_filename = task_folder + uid + '.txt'
        if UtilsFile.isPathExist(des_filename):
            return True

        return False
