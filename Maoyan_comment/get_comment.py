# -*- coding: utf-8 -*-
from __future__ import division
import csv
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
import time


driver = webdriver.PhantomJS('./phantomjs')

# 从csv文件中获取电影名字进行搜索
def get_movie_from_data():
    csv_reader = csv.reader(open('./movies_name.csv', 'r'))
    for line in csv_reader:
        jude = False
        movie_name = line[1]

        # 断点重续，开始时需要先建一个空文件
        with open('./data/had_checked.txt','r')as f:
            for line in f.readlines():
                if line.replace('\n','') == movie_name:
                    jude = True
                    continue
        if jude:
            continue
        if movie_name == 'movie_name':
            continue
        print movie_name
        # 先写列名
        save_data_to_csv(movie_name,jude,True)
        get_comment_page_url(movie_name)


# 从搜索页面中得到电影的ｉｄ
def get_comment_page_url(movie_name):
    url = 'http://maoyan.com/query?kw='+ urllib.quote(movie_name)+'&type=0'
    driver.get(url)
    movie_url = driver.find_elements_by_xpath('//div[@class="search-result-box"]/dl/dd/div[@class="channel-detail movie-item-title"]/a')
    # print movie_url[0]
    movie_id = movie_url[0].get_attribute("href").replace('http://maoyan.com/films/','')
    movie_comment_url = 'http://m.maoyan.com/movie/'+movie_id+'/comments'
    driver.get(movie_comment_url)
    get_comment(movie_name,movie_id)
    print movie_id
    # return movie_id


# 用电影ｉｄ进入到电影评论的手机版
def get_comment(movie_name,movie_id):

   # '''下滑５０次，得到更多的评论页面'''
    for i in range(50):
        time.sleep(2)
        try:
            driver.find_element('//div[@id="app"]/div[@class="layout"]/footer//span/')

        except:
            driver.execute_script("window.scrollTo(100000,document.body.scrollHeight);")
    print "50页信息已得到"



    '''获取评论信息'''
    users_info = driver.find_elements_by_xpath('//div[@class="pg-comments"]//li[@class="list-view-item "]/div')

    for user_info in users_info:
        information = {}
        try:
            information['movie_id'] = movie_id
            information['user_name'] = user_info.find_element_by_xpath('footer/em').text
            user_url = user_info.find_element_by_xpath('section/a').get_attribute("href")
            user_id = user_url.split('replies/')[-1].replace('?_v_=yes','')
            information['user_id'] = user_id
            information['comment'] = user_info.find_element_by_xpath('section/a/p').text
            information['time'] = user_info.find_element_by_xpath('header/time').get_attribute("title")
            information['good'] = user_info.find_element_by_xpath('footer/div/a[@class="link comment-like"]/span').text
            information['source'] = get_source(user_info)
            print information

            save_data_to_csv(movie_name, information,False)
            # return information
        except:
            continue

    with open('./data/had_checked.txt','a+')as f:
        f.write(movie_name+'\n')

# 得到用户评分
def get_source(response):
    source = 0
    pictures = response.find_elements_by_xpath('header/div/img')
    for picture in pictures:
        picture = picture.get_attribute("src")
        if picture == 'http://ms0.meituan.net/canary/img/star-full-new.png':
            source = source + 1
        if picture =='http://ms0.meituan.net/canary/img/star-half-new.png':
            source = source + 0.5
        if picture =='http://ms0.meituan.net/canary/img/star-empty-new.png':
            source = source
    return source


# 存储数据到csv文件，若type为True,则写入列名，否则按列名顺序存入数据
def save_data_to_csv(movie_name,information,type):

    with open('./data/'+movie_name+'.csv','a+') as csvfile:
        headers = ["movie_id", "user_name", "user_id", "comment", "time", "good", "source"]
        if type:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
        else:
            writer = csv.DictWriter(csvfile, headers)
            writer.writerow(information)



get_movie_from_data()


