#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: XmlRead.py
@time: 2019/1/9 17:17
@desc:
'''

from xml.dom.minidom import parse,parseString
import xml.dom.minidom

#miniDom 实现xml读写
DOMTree = parse("config\\movies.xml")

collection  = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("root element:"+collection.getAttribute("shelf"))
print("-------**************--------")
movies  = collection.getElementsByTagName("movie")
# print(movies) #返回指针
for movie  in movies:
    print("---Movises---")
    if movie.hasAttribute("title"):
        print("title is :" + movie.getAttribute("title"))
    type1 = movie.getElementsByTagName("type")[0]
    print("type is:" + type1.childNodes[0].data)
    format1 = movie.getElementsByTagName("format")[0]
    print("format is:" + format1.childNodes[0].data)
    rating  = movie.getElementsByTagName("rating")[0]
    print("rating is:"+rating.childNodes[0].data)
    des = movie.getElementsByTagName("description")[0]
    print("description is:"+des.childNodes[0].data)
