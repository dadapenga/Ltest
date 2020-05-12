#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: ZixunPara.py
@time: 2019/1/26 11:46
@desc:
'''
import random


def creatCount(mail,name):
    random1 = random.randint(15500000000,15599999999)
    creatCount = {
        "header": {},
        "request": {
            "c": "",
            "m": "",
            "p": {
                "src_id": 1,
                "name": name,
                "username": mail,
                "realname": name,
                "phone": random1
            }
        }
    }
    return creatCount

def openPro(manage_id,product_id):
    openProd = {
        "header": {
        },
        "request": {
            "c": "",
            "m": "",
            "p": {
                "company_id":manage_id,
                "product_id": product_id,
                "deadline": 0
            }
        }
    }
    return openProd