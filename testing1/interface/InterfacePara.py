#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: InterfacePara.py
@time: 2019/1/5 14:35
@desc:
'''
import json
import random
import configparser

conf = configparser.ConfigParser()
conf.read("C:\\Users\\5w8x93x\\PycharmProjects\\test1\\testing1\\config\\config.ini");
session = conf.get("interface", "session")
phone = conf.get("interface", "phone")
managerId = conf.getint("interface", "managerId")
switch = conf.getint("interface", "switch")
# phone ="18877889911"
# managerId=32
code = phone[0] + phone[2] + phone[4] + phone[6] + phone[8] + phone[10]


def login_get_code():
    random1 = random.randint(8888888, 9999999)
    values = {
        "header": {
            "appid": 20,
            "log_id": str(random1),
            "uid": "",
            "uname": "",
            "provider": "",
            "signid": "",
            "version": "",
            "ip": ""
        },
        "request": {
            "w": "",
            "c": "",
            "m": "",
            "p": {
                "phone": str(phone)
            }
        }
    }
    print(values)
    return values


def login():
    random1 = random.randint(8888888, 9999999)
    values = {
        "header": {
            "appid": 20,
            "log_id": str(random1),
            "uid": "",
            "uname": "",
            "provider": "",
            "signid": "",
            "version": "",
            "ip": ""
        },
        "request": {
            "w": "",
            "c": "",
            "m": "",
            "p": {
                "src_id": 1,
                "manager_id": managerId,
                "phone": str(phone),
                "auth_code": str(code)
            }
        }
    }
    print(values)
    return values


def win_mainpage(session1):
    random1 = random.randint(8888888, 9999999)
    values = {
        "header": {
            "appid": 20,
            "log_id": str(random1),
            "uid": "",
            "uname": "",
            "provider": "",
            "signid": "",
            "version": "",
            "ip": ""
        },
        "request": {
            "w": "",
            "c": "",
            "m": "",
            "p": {
                "session": session1
            }
        }
    }
    print(values)
    return values


def win_exam_begin(i, session1):
    random1 = random.randint(8888888, 9999999)
    values = {"header": {
        "appid": 20,
        "log_id": str(random1),
        "uid": "",
        "uname": "",
        "provider": "",
        "signid": "",
        "version": "",
        "ip": ""
    },
        "request": {
            "w": "",
            "c": "",
            "m": "",
            "p": {
                "session": session1,
                "axis0": i
            }
        }
    }
    print(values)
    return values


def win_step_commit1(session, i, questionID, type, optionsid=[], ):
    if len(optionsid) == 5:
        if switch == 1:
            random.shuffle(optionsid)
        options = [{
            "option_id": optionsid[0],
            "text": "完全不认同",
            "has_choice": False
        }, {
            "option_id": optionsid[1],
            "text": "非常不认同",
            "has_choice": False
        }, {
            "option_id": optionsid[2],
            "text": "稍有不认同",
            "has_choice": False
        }, {
            "option_id": optionsid[3],
            "text": "基本认同",
            "has_choice": False
        }, {
            "option_id": optionsid[4],
            "text": "特别认同",
            "has_choice": True
        }]
    elif len(optionsid) == 4:
        if switch == 1:
            random.shuffle(optionsid)
        options = [{
            "option_id": optionsid[0],
            "text": "从不",
            "has_choice": False
        }, {
            "option_id": optionsid[1],
            "text": "极少",
            "has_choice": False
        }, {
            "option_id": optionsid[2],
            "text": "偶尔",
            "has_choice": False
        }, {
            "option_id": optionsid[3],
            "text": "经常",
            "has_choice": True
        }]
    else:
        options = [{
            "option_id": 1001101,
            "text": "客户亲密",
            "has_choice": False
        }, {
            "option_id": 1001102,
            "text": "精益运营",
            "has_choice": False
        }, {
            "option_id": 1001103,
            "text": "技术创新",
            "has_choice": True
        }]
    values = {
        "header": {
            "appid": 20,
            "log_id": str(random.randint(8888888, 9999999)),
            "uid": "",
            "uname": "",
            "provider": "",
            "signid": "",
            "version": "",
            "ip": ""
        },
        "request": {
            "w": "",
            "c": "",
            "m": "",
            "p": {
                "session": session,
                "axis0": i,
                "question": {
                    "question_id": questionID,
                    "text": "您认同公司目前管理有效、运作良好吗？",
                    "type": type,
                    "has_answer": True,
                    "options": options
                }
            }
        }
    }
    print(values)
    return values


def win_step_commit2(session, i, questionID, type, ):
    values = {
        "header": {
            "appid": 20,
            "log_id": random.randint(8888888, 9999999),
            "uid": "",
            "uname": "",
            "provider": "",
            "signid": "",
            "version": "",
            "ip": ""
        },
        "request": {
            "w": "",
            "c": "",
            "m": "",
            "p": {
                "session": session,
                "axis0": i,
                "question": {
                    "question_id": questionID,
                    "text": "您认为一年内公司最为关键的业务活动是什么？",
                    "type": type,
                    "has_answer": True,
                    "answer": "拉拉吧巴巴爸爸吧☆彡(^･ᴗ･^)新年快乐"
                }
            }
        }
    }

# options = [{
#     "option_id": optionsid[0],
#     "text": "完全不认同",
#     "has_choice": True
# }, {
#     "option_id": optionsid[1],
#     "text": "非常不认同",
#     "has_choice": False
# }, {
#     "option_id": optionsid[2],
#     "text": "稍有不认同",
#     "has_choice": False
# }, {
#     "option_id": optionsid[3],
#     "text": "基本认同",
#     "has_choice": False
# }, {
#     "option_id": optionsid[4],
#     "text": "特别认同",
#     "has_choice": False
# }]
