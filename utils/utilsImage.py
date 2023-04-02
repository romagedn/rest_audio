
import os
import argparse
from PIL import Image, ImageDraw, ImageFont
from utils.utilsFile import UtilsFile
import matplotlib.pyplot as pyplot
import matplotlib.image as mat_image
import sys



class UtilsImage:

    @staticmethod
    def combine2one(filelist:list, filename, col, row, width, height, deleteSource=True, positions=None, stretch=2):
        '''

        :param filelist:
        :param filename:
        :param col:
        :param row:
        :param width:
        :param height:
        :param deleteSource:
        :param positions:
        :param stretch: 0 - no scale; 1 - scalex = scaley; 2 - scalex, scaley are independent
        :return:
        '''

        save_image = Image.new('RGBA', (width, height), color=(255, 255, 255))
        piece_w = int(width / col)
        piece_h = int(height / row)

        index = 0
        for image_name in filelist:
            image = Image.open(image_name)

            if stretch == 1:
                # 按宽高最小的匹配，保证不超界，不变形
                scaleX = min(piece_w / image.size[0], piece_h / image.size[1])
                scaleY = scaleX
            elif stretch == 2:
                # 宽高独立调整，可能变形
                scaleX = piece_w / image.size[0]
                scaleY = piece_h / image.size[1]
            elif stretch == 3:
                # 按宽高最小的匹配，保证不超界，不变形
                # 只放大，不缩小
                scaleX = min(piece_w / image.size[0], piece_h / image.size[1], 1)
                scaleY = scaleX
            else:
                # 不调整
                scaleX = 1
                scaleY = scaleX

            size = (int(image.size[0] * scaleX), int(image.size[1] * scaleY))
            image = image.resize(size)

            if positions is None:
                x = int(index % col) * piece_w
                y = int(index / col) * piece_h
            else:
                x = positions[index][0] * piece_w
                y = positions[index][1] * piece_h
            index += 1

            save_image.paste(image, (x, y))
            image.close()

        if '.jpg' in filename:
            save_image = save_image.convert('RGB')
        save_image.save(filename)
        save_image.close()

        if deleteSource:
            for image_name in filelist:
                UtilsFile.delFile(image_name)


    @staticmethod
    def showImg(filename, onlyShowInNotebook=True):
        if onlyShowInNotebook:
            if '.ipynb' not in sys.argv[0] and 'ipykernel_launcher.py' not in sys.argv[0]:
                return

        pic = mat_image.imread(filename)  # 读取和代码处于同一目录下的 lena.png
        # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
        # lena.shape  # (512, 512, 3)

        pyplot.figure()
        pyplot.imshow(pic)  # 显示图片
        pyplot.axis('off')  # 不显示坐标轴
        pyplot.show()
        pyplot.close('all')


