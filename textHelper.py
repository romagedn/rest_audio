
# !/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : xxx
#   Email         : xxx@gmail.com
#   File Name     : check_chinese_and_symbol.py
#   Last Modified : 2020-06-03 18:11
#   Description   :
#
# ====================================================

import sys
# import os

import re

from zhon.hanzi import punctuation
from zhon.hanzi import characters

def lm_find_unchinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    unchinese = re.sub(pattern ,"" ,file)  # 排除汉字
    unchinese = re.sub('[{}]'.format(punctuation) ,"" ,unchinese)  # 排除中文符号
    # print("unchinese:",unchinese)
    return unchinese


def lm_find_chinese(m_str):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', m_str)
    print("chinese:" ,chinese)

def lm_find_chinese_symbol(m_str):
    t_symbol = re.findall("[{}]".format(punctuation) ,m_str)
    print("chinese symbols:" ,t_symbol)

def lm_find_chinese_and_symbol(m_str):
    lm_find_unchinese(m_str)
    lm_find_chinese(m_str)
    lm_find_chinese_symbol(m_str)

def lm_delete_chinese_and_symbol(m_str):
    print("delete chinese and symbol")

# 测试用例
def test():
    fp = open("./CenterCrop.frag" ,"r+")
    content = fp.read()
    print("查找到的中文符号：" ,re.findall("[{}]".format(punctuation) ,content))
    print("中文汉字：" ,re.findall("[{}]".format(characters) ,content))
    lm_find_chinese(content)
    unchinese =  lm_find_unchinese(content)
    fp.seek(0 ,0)
    fp.truncate()
    fp.write(unchinese)
    fp.close()

def main(argv=None):
    #    lm_find_chinese_and_symbol(line)
    print("main")

if __name__ == "__main__":
    sys.exit(main())
