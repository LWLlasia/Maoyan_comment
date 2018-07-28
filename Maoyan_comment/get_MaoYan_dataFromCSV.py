# -*- coding: utf-8 -*-
from __future__ import division
import csv
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

# 从csv文件中读取数据

def get_Maoyan_from_csv():
    for root,dirs,files in os.walk('./data'):
        # print root #当前目录路径
        # print dirs #当前路径下所有子目录
        # print files  #当前路径下所有非目录子文件
        for name in files:
            if '.csv' in name:
                csv_reader = csv.DictReader(open('./data/'+name))
                for row in csv_reader:
                    # print row #返回整个字典
                    # print row['movie_id']
                    # print row['user_name']
                    # print row['user_id']
                    # print row['comment']
                    # print row['time']
                    # print row['good']
                    # print row['source']

                    # 需要什么数据就return什么
                    return row['movie_id'],row['user_name'],row['user_id'],row['comment'],row['time'],row['good'],row['source']


get_Maoyan_from_csv()





