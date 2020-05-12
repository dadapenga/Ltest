#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: crawl.py
@time: 2018/12/11 13:40
@desc:
'''

import configparser
import random

# conf = configparser.ConfigParser()
# conf.read("config\\config.ini");
# session = conf.get("interface", "session")
# print(session)
# phone = conf.get("interface", "phone")
# print(phone)

options = [{
    "option_id": 1,
    "text": "完全不认同",
    "has_choice": True
}, {
    "option_id": 2,
    "text": "非常不认同",
    "has_choice": False
}, {
    "option_id": 3,
    "text": "稍有不认同",
    "has_choice": False
}, {
    "option_id": 4,
    "text": "基本认同",
    "has_choice": False
}, {
    "option_id": 5,
    "text": "特别认同",
    "has_choice": False
}]
print(options)

random.shuffle(options)
print(options)