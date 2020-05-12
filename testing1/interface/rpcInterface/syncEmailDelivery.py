#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: syncEmailDelivery.py
@time: 2019/4/9 10:13
@desc:
'''

import json, time, requests, random, sys, os

environment_type = 't'

class tob_rpc():
    def __init__(self):
        pass

    def tob_delivery_inner(self):
        url = '/atsng/rpc'
        api = rpcAPI(environment_type, url)
        '''$p = [
        'icdc_resume_id' = > 1, // icdc简历id  必填
        'uid' = > 81, // 需要同步的tob帐号uid 必填
        'position_name' = > '网络工程师', // 职位名称  必填
        'city_name' = > '', // 城市名称
        'sourceJidFrom' = > 11, // 投递渠道 必填
        'deliveryTime' = > time(), // 投递时间  必填
        'email' = > 'zhongchi.li@ifchange.com', // 邮箱用户名   必填
        'password' = > 'Lizhongchi08', // 邮箱密码  必填
        'subject' = > '网络工程师：张明的简历（来自拉勾）', // 邮件主题   必填
        'ifchange_position_ids' = > '', // 基础数据职位ID，兼容参数
        ];'''
        api.params = {
            "request": {
                "p": {
                    "icdc_resume_id": "lp测试职位3",
                    "uid": "上海",
                    "position_name": "",
                    "city_name": "",
                    "sourceJidFrom": 1,
                    "deliveryTime": "",
                    "email": "",
                    "password": "",
                    "subject": 1,
                    "ifchange_position_ids": "docx",
                },
                "c": "delivery",
                "m": "syncEmailDelivery"
            },
            "header": {
                "provider": "testing_aide",
                "uid": 1226
            }
        }
        result = api.do_test()




class rpcAPI():
    params = {}

    def __init__(self, test_type, api_url, base_url=''):
        self.api_url = api_url
        self.test_type = test_type

        if test_type == 't':
            if base_url == '':
                self.base_url = 'http://testing2.common-ats.rpc'
        else:
            if base_url == '':
                self.base_url = 'http://common-ats.rpc'

    def do_test(self, datatype='json'):
        start_time = time.time()
        if datatype != 'json':
            r = requests.post(self.base_url + self.api_url, data=self.params)
        else:
            r = requests.post(self.base_url + self.api_url, json=self.params)
        response = r.text
        end_time = time.time()
        print(response)
        return json.loads(response)


if __name__ == "__main__":
    obj = tob_rpc()
    obj.tob_delivery_inner()


