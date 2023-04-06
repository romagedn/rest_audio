import paddlehub as hub
import os
import json

from textHelper import *
from utils.arguments import Arguments
from utils.utilsFile import UtilsFile
from utils.utilsTime import UtilsTime


def findNextTask(path):
    # allFile = []

    fileList = os.listdir(path)
    for fileName in fileList:
        if not fileName.lower().endswith(".txt"):
            continue

        filePath = os.path.join(path, fileName)
        if not os.path.isdir(filePath):
            return filePath

    return None


def loadTaskContent(path):
    content = UtilsFile.readFileContent(path)
    content = json.loads(content)
    return content


def deleteTask(filePath):
    try:
        if UtilsFile.isPathExist(filePath):
            content = UtilsFile.readFileContent(filePath)
            content = json.loads(content)
            sample_file = content['sample_file']
            message = content['message']
            if UtilsFile.isPathExist(sample_file):
                UtilsFile.delFile(sample_file)
            UtilsFile.delFile(filePath)
    except:
        print('fail to delete task', filePath)


def correctText2Chinese(s:str):
    s = s.replace(',', '，')
    s = s.replace('.', '。')
    s = s.replace(';', '；')
    s = s.replace(':', '：')
    s = s.replace('"', '“')
    s = s.replace("'", "‘")
    s = s.replace('?', '？')
    s = s.replace('!', '！')
    s = s.replace('(', '（')
    s = s.replace(')', '}')
    s = s.replace('[', '【')
    s = s.replace(']', '】')
    s = lm_find_chinese(s)

    s = s.replace('，', '$')
    s = s.replace('。', '$')
    s = s.replace('；', '$')
    s = s.replace('：', '$')
    s = s.replace('“', '$')
    s = s.replace("‘", '$')
    s = s.replace('？', '$')
    s = s.replace('！', '$')
    s = s.replace('（', '$')
    s = s.replace('}', '$')
    s = s.replace('【', '$')
    s = s.replace('】', '$')

    s = s.replace('\n', '$')
    return s


def correct_text(text, max_length=60):
    text = correctText2Chinese(text)

    texts = []
    while len(text) > max_length:
        _text = text[:max_length]
        text = text[max_length:]
        texts.append(_text)
    return texts


def build():
    # 定义目标音色，加载模型
    filePath = findNextTask(task_folder)
    if filePath is None:
        return None

    try:
        fileName = os.path.basename(filePath)
        baseName = os.path.splitext(fileName)[0]

        content:dict = loadTaskContent(filePath)
        sample_file = content['sample_file']
        message = content['message']

        filename_sample_audio = os.path.join(task_folder, sample_file)
        model = hub.Module(name='lstm_tacotron2',
                           output_dir=output_folder,
                           speaker_audio=filename_sample_audio)  # 指定目标音色音频文件

        # 使用generate()函数得到最终合成语音
        texts = correct_text(message)
        wavs = model.generate(texts, use_gpu=True)

        dsts = []
        for wav in wavs:
            dst = filePath + baseName + '_{}.wav'.format(len(dsts))
            dsts.append(dst)
            UtilsFile.copyFile(wav, dst)

        des = content.copy()
        des.update({
            'speech_texts': texts,
            'speech_wavs': dsts,
        })
        dst = filePath + fileName
        UtilsFile.writeFileLines(dst, [json.dumps(des)])

        print('done task', filePath)

        deleteTask(filePath)
        return [texts, wavs]

    except:
        deleteTask(filePath)
        return None


if __name__ == '__main__':
    argument = Arguments()
    print('command line')
    print(argument.getCommandLine())
    print('')

    task_folder = './_temp_/'
    output_folder = './_output_/'

    texts, wavs = build()

