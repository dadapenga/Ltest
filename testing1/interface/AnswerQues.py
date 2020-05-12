#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: AnswerQues.py
@time: 2019/1/5 10:41
@desc:winmode
'''

import requests
import random
from testing1.interface import InterfacePara

urlgetcode = "https://bot.testing2.ifchange.com/api/login/get_auth_code"
urllogin = "https://bot.testing2.ifchange.com/api/login/auth_code_login"
urlmainpage = "https://bot.testing2.ifchange.com/api/winmode/main_page"
urlExambegan = "https://bot.testing2.ifchange.com/api/winmode/exam_begin"
urlCommit = "https://bot.testing2.ifchange.com/api/winmode/exam_step_commit"
urlfinish = "https://bot.testing2.ifchange.com/api/winmode/exam_finish"

headers1 = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
headers ={
        "appid": 20,
        "log_id": str(random.randint(8888888, 9999999)),
        "uid": "",
        "uname": "",
        "provider": "",
        "signid": "",
        "version": "",
        "ip": ""
    }
print("开始获取验证码")
urlgetcodeRe = requests.post(urlgetcode,json=InterfacePara.login_get_code())
print("获取验证码接口返回")
print(urlgetcodeRe.text)

print("开始验证登陆")
urlloginRe =requests.post(urllogin,json=InterfacePara.login())
print("登陆验证返回")
print(urlloginRe.text)

print("取登陆接口的返回值session为")
session = urlloginRe.json().get("response").get("results").get("session")
print(session)

print("mainpage接口开始调用")
urlmainpageRe = requests.post(urlmainpage,json=InterfacePara.win_mainpage(session))
print("mainpage接口返回为")
print(urlmainpageRe.text)

for i in range(1, 4):
    print("测验开始接口开始调用,次数为：" + str(i))
    urlExamBeganRe = requests.post(urlExambegan, json=InterfacePara.win_exam_begin(i, session))
    print("测验开始接口调用返回值为")
    print(urlExamBeganRe.text)
    questions = urlExamBeganRe.json().get("response").get("results").get("questions")
    for question in questions:
        questionId = question.get("question_id")
        quesType = question.get("type")
        if quesType == 0:
            options = question.get("options")
            quesOptions = []
            for option in options:
                quesOptions.append(option.get("option_id"))
            print("开始提交答案，题号为：" + str(questionId))
            urlCommitRe = requests.post(urlCommit,
                                        json=InterfacePara.win_step_commit1(session, i, questionId, quesType,
                                                                            optionsid=quesOptions))
            print("提交答案的返回")
            print(urlCommitRe.text)
        else:
            print("开始提交答案，题号为：" + str(questionId))
            urlCommitRe = requests.post(urlCommit,
                                        json=InterfacePara.win_step_commit2(session, i, questionId, quesType))
            print("提交答案的返回")
            print(urlCommitRe.text)
    print("开始请求测验结束接口")
    urlExamFinishRe = requests.post(urlfinish, json=InterfacePara.win_exam_begin(i, session))
    print("测验结束接口返回")
    print(urlExamFinishRe.text)
print("end")






