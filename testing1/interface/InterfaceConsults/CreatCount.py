#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: CreatCount.py
@time: 2019/1/26 10:59
@desc:
'''
import requests
import json
from testing1.interface.InterfaceConsults import ZixunPara
headers ={"X":"SUu5V7NPXQXzI8wCL95LYV9IkZdnzGfQ"}
env="https://bot.testing2.ifchange.com"
urlCreCount = env + "/api/admin/managers/save"
urlOpenProd = env + "/api/admin/companies/assignproduct"

def creatCount(mail,name,next=None):
    creCountRe = requests.post(urlCreCount, headers=headers, json=ZixunPara.creatCount(mail, name))
    print(creCountRe.text)
    manager_id = creCountRe.json().get("response").get("results").get("manager_id")
    password = creCountRe.json().get("response").get("results").get("password")
    print("开通账号成功，账号为："+mail+"。密码为："+password+"。manager_id为："+str(manager_id))
    if next is not None:
        openProd(manager_id,next)


def openProd(manager_id,prod_id):
    for prod in prod_id:
        openProdRe = requests.post(urlOpenProd, headers=headers, json=ZixunPara.openPro(manager_id,prod ))
        print("开通成功")

if __name__ =='__main__':
    creatCount("peng.liu18@ifchange.com", "test3221", [3,10] )