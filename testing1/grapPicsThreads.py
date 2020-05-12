#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: grapPicsThreads.py
@time: 2018/11/28 13:56
@desc:
'''
import urllib
import urllib.request
import re
import configparser
import csv
import logging
from atexit import register

from testing1 import MyThread
import threading
import requests
from bs4 import BeautifulSoup

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#配置文件读取
conf = configparser.ConfigParser();
conf.read("config\\config.ini");
#通过配置文件
power = conf.getint("grapPic","n")
logfile = conf.get("grapPic","logfile")




#日志文件配置
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename=logfile, level=logging.INFO, format=LOG_FORMAT,datefmt=DATE_FORMAT)  #在basicConfig源码1806行设置了默认的编码格式UTF-8  解决中文在日志中乱码的问题

logging.info("the power is :"+str(power))
level= 1

#请求url
def getHtml(url):
    logging.info("start to get html:"+url)
    try:
        page = requests.get(url,timeout= 3)
        html = page.text
        return html
    except Exception as e:
        print(str(e))
        logging.error(url+"bad url:"+str(e))
        return None

# def getHtml(url):             #有乱码很烦
#     logging.info("开始获取html："+str(url))
#     try:
#         page = urllib.request.urlopen(url,timeout=3);
#         html = page.read()
#         return html.decode('UTF-8')
#     except Exception as e:
#         print(str(e))
#         logging.error(url+"  :   "+str(e))
#         return None


#读取csv文件  返回list
def readCSV(file):
    csv_reader = csv.reader(open(file,'r'))      #url中的编码问题待解决   gbk  unicode   utf-8  ,encoding="UTF-8"
    csvLine = []
    logging.info("read --csv："+ file)
    for row in csv_reader:
        csvLine.append(row);
    return  csvLine;

#写入allcsv文件
def writeCSVA( file,data):
    try:
        lock.acquire()
        csv_writer = csv.writer( open(file,'a',newline='',encoding="UTF-8"))    #add书写    写入csv文件的时候也会有编码格式的问题  待解决
        # MyThread.MyThread(csv_writer.writerow,(data,))
        csv_writer.writerow(data)
        lock.release()
    except Exception as e:
        print(str(e))
        logging.error("writeCSVerror , on :"+file+". data:" + str(data))

#写入csv文件
def writeCSVW( file,data):
    csv_writer = csv.writer( open(file,'w',newline='',encoding= "UTF-8"))    #w书写   没用到
    csv_writer.writerow(data)

#保存图片
def savePics(picList):
    #保存图片
    path = "D:\\testdir\\"
    for imagrUrl in picList:
        try:
            # pathImg= path+str(level)+'_pics_'+str(picList.index(imagrUrl))+'_'+imagrUrl.split('/')[-1]
            # imagrUrl=imagrUrl.replace("\\", '')
            # MyThread.MyThread(urllib.request.urlretrieve, (imagrUrl, pathImg))    #MyThread继承Thread类  传入参数为方法，参数，方法名 调用之后自动运行run函数中的方法
            urllib.request.urlretrieve(imagrUrl.replace("\\", ''), path+str(level)+'_pics_'+str(picList.index(imagrUrl))+'_'+imagrUrl.split('/')[-1]);

            print("savepic success "+imagrUrl)
            logging.info("savepic success"+str(imagrUrl))
            #保存图片到本地   urlretrieve方法
        except Exception as e:
            print(str(e),imagrUrl)
            logging.error("savepic error:",str(imagrUrl),e )


#保存url  W
def saveUrl(urlList,control1 = 0):
    con = level+control1
    for url in  urlList:
        url = [url]
        writeCSVA("data\\urlList"+str(con)+".csv",url)

#保存所有url
def saveAllUrl(urlList):
    for url in  urlList:
        url = [url]
        writeCSVA("data\\urlListAll.csv",url)

#匹配图片
def matchPics(html):
    #匹配图片格式
    reg =r'http[^\s]*.(?:jpg|png)'                          #r''''|"((http|https|//|/).*?(.jpg|.jpeg|.gif|.png|.bmp))('|")'''      # "http.*?\.png|http.*?\.jpg"  ;#       '"imgUrl": "(http.*?\.jpg)"'
    regli = re.compile(reg);
    reglist = list(set(regli.findall(html)))
    return  reglist

#匹配图片  beautifuls4
# def matchPics(html,url):
#     url1 = url[:-1]
#     soup = BeautifulSoup(html,features="html.parser")
#     picList= []
#     try:
#         for pics in soup.find_all('img'):
#             pic = pics.get("src")
#             picList.append(pic)
#         print(picList)
#     except Exception as e:
#         print(str(e))
#         logging.error("查图片的exception")
#     return picList




#匹配外链的a标签中  href   beautifulSoup
def matchHref(html,preURL):
    soup = BeautifulSoup(html,features="html.parser")
    hrefList = []
    url = preURL[:-1]
    for link in soup.find_all("a"):
        href = link.get("href")
        if str(href).startswith("http"):
            hrefList.append(href)
        else:
            if str(href).startswith("/"):
                hrefList.append(url+str(href))
    hrefList = list(set(hrefList))
    return hrefList


#匹配外链的url
# def matchHref(html):
#     compileRuler = re.compile(r"<a.*?href=https://|http://.*? ")
#     urlList = compileRuler.findall(html)
#     urlList = list(set(urlList))
#     return urlList


#锁内的代码串行化
lock = threading.Lock()

if __name__ == '__main__':
    # 读取并保存 配置中的url
    urlListPre = readCSV("data\\urls.csv")
    for url in urlListPre:
        url = url[0]  # csv文件读出来的每一行是一个list
        html = getHtml(url)  # 得到url中的html
        savePics(matchPics(html))  # 保存url中的图片
        matchHrefs = matchHref(html,url)  # 得到html中的链接
        saveAllUrl(matchHrefs)  # 保存所有的url到   urlListAll.csv
        saveUrl(matchHrefs)  # 保存这一层的url  全局变量level控制

# 读取保存的url

    for level in range(1, power):
        # urlsList = readCSV("data\\urlList" + str(level) + ".csv")  # list承接的下这么大的数据量？ 5w+
        Csv_reader = csv.reader(
            open("data\\urllist" + str(level) + ".csv", "r", encoding="UTF-8"))  # 直接读csv文件    一行一行的进行遍历url中的文件
        for row in Csv_reader:
            # level = level + 1  # 控制读取的和保存的csv层级
            # for url in urlsList:
            #     url = url[0]
            url = row[0]
            html = getHtml(url)
            if html == None:
                logging.warning("return null ,continue")
                continue
            picList = matchPics(html)  # 返回picList
            # MyThread.MyThread(savePics, (picList,))  # 保存图片
            savePics(picList)

            matchHrefs = matchHref(html, url)  # 返回urlList
            MyThread.MyThread(saveAllUrl, (matchHrefs,)).start()  # 保存所有的url
            MyThread.MyThread(saveUrl, (matchHrefs, 1)).start()  # 保存单个层级的url


        level = level + 1

@register                        #退出函数  在线程完成之后主线程退出
def _atexit():
    print("all done")
