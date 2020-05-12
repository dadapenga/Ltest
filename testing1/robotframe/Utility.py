#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: Utility.py
@time: 2019/5/6 17:56
@desc:
'''
import json
import time, random, datetime

import requests


class Utility():
    def printTime(self, ):
        # 时间戳
        t = int(time.time())
        print(int(t))
        return t

    def mailDelivery(self, environment='t', ):
        para = {}
        t = int(time.time())
        idefine = random.randint(1000, 9999)
        onlyId = str(idefine) + str(datetime.datetime.now().month) + str(datetime.datetime.now().day)

        month = datetime.datetime.now().month %10
        day= datetime.datetime.now().day%10
        phone = "13" + str(month) +str(day) + str(random.randint(100, 999)) + str(random.randint(1000, 9999))

        url = ''
        # 简历信息 原始简历和简历信息
        content = "{\"source\":{\"src\":\"1\",\"src_no\":\"" + str(
            t) + "\"},\"contact\":{\"phone\":\"" + phone + "\",\"email\":\"lpt" + onlyId + "@163.com\"},\"basic\":{\"resume_name\":\"lp\\u90ae\\u4ef6\\u6d4b\\u8bd521\\u7684\\u7b80\\u5386\",\"name\":\"lp\\u90ae" + onlyId + "\",\"gender\":\"M\",\"work_experience\":\"6\",\"birth\":\"1989\\u5e7410\\u6708\",\"age\":\"30\",\"expect_type\":\"\\u5168\\u804c\",\"address\":\"105\",\"expect_position_name\":\"PHP\",\"current_status\":\"1\",\"updated_at\":\"2019-02-19 19:09:00\",\"expect_city_ids\":\"105\",\"expect_salary_from\":\"15\",\"expect_salary_to\":\"30\"}}"
        original_content1 = "ZnJvbV9qc29uX2VuY29kZV9yZXN1bHQ6eyJzdGF0ZSI6MSwibWVzc2FnZSI6IuaTjeS9nOaIkOWKnyIsImNvbnRlbnQiOnsiZGF0YSI6eyJwb3NpdGlvbk5hbWUiOiLnvZHnu5zlt6XnqIvluIgiLCJkZWxpdmVyVGltZSI6IjIwMTktMDItMjUgMTk6NDciLCJwb3NpdGlvbklkIjo0NDE2NjA2LCJoYXZlSW50ZXJ2aWV3IjpmYWxzZSwicmVzdW1lVmVyc2lvbiI6IlY0IiwieXVuc3RhdHVzIjoiIiwicmVzdW1lVm8iOnsiaWQiOiI1YzZiZTUwMjE4MjNjZTMzN2JjYjlhOTYiLCJzZXgiOiLnlLciLCJiaXJ0aGRheSI6IjE5ODkuMTAiLCJiaXJ0aFllYXIiOjE5ODksImJpcnRoTW9udGgiOiIxMCIsImJpcnRoRGF0ZSI6IjEiLCJhZ2VOdW0iOjMwLCJ3b3JrWWVhciI6IjblubQiLCJwaG9uZSI6IjE1ODIxNzc1Mjc4IiwiZW1haWwiOiJkYW5tZHJAMTYzLmNvbSIsInN0YXR1cyI6IuaIkeebruWJjeW3suemu+iBjO+8jOWPr+W\/q+mAn+WIsOWylyIsIm15UmVtYXJrIjoiPHVsPiBcbiA8bGk+PHA+Jm5ic3A75pys5Lq65oSP5ZCR55S15ZWG5oiW6auY5bm25Y+R77yM6LSj5Lu75b+D6Z2e5bi45by677yM6ICQ5Yqb5oyB5LmF77yM54Ot54ix5oqA5pyv77yM55qu5a6e44CC5pys5Lq656ym5ZCI56iL5bqP5ZGY54m55b6B5YaF5pWb44CB54G15rS744CB5omn552A44CC54Ot6KG35LqO5oqA5pyv77yM5bSH5bCa56eR5oqA5pS55Y+Y5LiW55WM44CCJm5ic3A7PGJyIC8+PC9wPjwvbGk+XG48L3VsPiIsInJlc3VtZU5hbWUiOiLlvKDmmI7nmoTnroDljoYiLCJuYW1lIjoi5byg5piOIiwibmFtZURlcyI6IiIsImNyZWF0ZVRpbWUiOiIyMDE5MDIxOVQxOTAzNDArMDgwMCIsInVwZGF0ZVRpbWUiOiIyMDE5MDIxOVQxOTA5MjgrMDgwMCIsInJlZnJlc2hUaW1lIjoiMjAxOS0wMi0xOSAxOTowOSIsInBlcmZlY3QiOiIxMTExMDEwMTExMDAwMDAxMTExMDAwMDAxMTEwMDAxMDExMDAxMTExMTAxMSIsImhlYWRQaWMiOiJjb21tb24vaW1hZ2UvcGMvZGVmYXVsdF9ib3lfaGVhZHBpYzMucG5nIiwidXNlcklkIjo0OTA4MTQ1LCJoaWdoZXN0RWR1Y2F0aW9uIjoi5pys56eRIiwib25lV29yZCI6IuWBmuS6i+iupOecn+OAgei0n+i0o++8jOazqOmHjeWboumYn+WQiOS9nOOAgiIsImxpdmVDaXR5Ijoi5LiK5rW3IiwidXNlcklkZW50aXR5IjoyLCJyZXN1bWVJZCI6Mzk4NjQ2NSwicmVzdW1lU2NvcmUiOi0xLCJyZXN1bWVLZXkiOiIiLCJjb21wYW55TmFtZSI6IuS4nOiOnue+juWunOS9syIsIndvcmtFeHBlcmllbmNlcyI6W3siY29tcGFueU5hbWUiOiLoh7PlloTnvZHnu5zogqHku73mnInpmZDlhazlj7giLCJwb3NpdGlvbk5hbWUiOiJQSFAiLCJzdGFydERhdGUiOiIyMDEzLjAzIiwiZW5kRGF0ZSI6IjIwMTYuMDQiLCJjcmVhdGVUaW1lIj"
        original_content2 = "oiMjAxNjA0MjVUMDEzNzA2KzA4MDAiLCJ3b3JrQ29udGVudCI6IjxwPiZuYnNwO+S\/oeaJmOWfuue6v+eJiDQuMCDliY3nq6\/lvIDlj5Hlt6XnqIvluIgg5oGS55Sf55S15a2Q6IKh5Lu95pyJ6ZmQ5YWs5Y+4IOS4u+imgei0n+i0o+S7u+WKoe+8miDlj4LkuI7kv6HmiZjkuJrliqHnmoTliLblrprvvIzmlbTlkIjkvJjnp4Dkv6HmiZjlhazlj7jova\/ku7bnmoTnibnngrnvvJsg5Yi25a6a5Z+657q\/54mI5byA5Y+R55qE5Lu75Yqh6KeE5YiS77yM5bm25Y+C5LiO5byA5Y+R77ybIOWNj+iwg+a1i+ivlee8luWGmea1i+ivleeUqOS+i++8myDmioDmnK\/vvJpsaWdodCArIHZ1ZSArIHdlZXgg5pS26I6377yaIOWNj+iwg+ayn+mAmuihqOi+vuiDveWKm+W+l+WIsOS6huW+iOWkp+eahOaPkOmrmO+8myDov5vkuIDmraXmjozmj6Hkv6HmiZjkuJrliqHmqKHlnZfvvJrnlLXlrZDlkIjlkIzvvIzkv6Hmga\/miqvpnLLvvIzlrp7lkI3orqTor4HnrYnvvJsg54af5oKJ5L+h5omY55qE5Lqk5piT5rWB56iL77ya6K+35rGC4oCUJmd0O1RBJmFncmF2ZTvpk7bogZTmiaPmrL7igJQmZ3Q76L+U5ZueVEEmbmJzcDs8YnIgLz48L3A+IiwiZGVwYXJ0bWVudCI6IueglOWPkSIsInNraWxsTGFiZWxzIjpbIuWQjuerryIsIuacjeWKoeWZqOerryJdfV0sImxhdGVzdFdvcmtFeHBlcmllbmNlIjp7ImNvbXBhbnlOYW1lIjoi6Iez5ZaE572R57uc6IKh5Lu95pyJ6ZmQ5YWs5Y+4IiwicG9zaXRpb25OYW1lIjoiUEhQIiwic3RhcnREYXRlIjoiMjAxMy4wMyIsImVuZERhdGUiOiIyMDE2LjA0IiwiY3JlYXRlVGltZSI6IjIwMTYwNDI1VDAxMzcwNiswODAwIiwid29ya0NvbnRlbnQiOiI8cD4mbmJzcDvkv6HmiZjln7rnur\/niYg0LjAg5YmN56uv5byA5Y+R5bel56iL5biIIOaBkueUn+eUteWtkOiCoeS7veaciemZkOWFrOWPuCDkuLvopoHotJ\/otKPku7vliqHvvJog5Y+C5LiO5L+h5omY5Lia5Yqh55qE5Yi25a6a77yM5pW05ZCI5LyY56eA5L+h5omY5YWs5Y+46L2v5Lu255qE54m554K577ybIOWItuWumuWfuue6v+eJiOW8gOWPkeeahOS7u+WKoeinhOWIku+8jOW5tuWPguS4juW8gOWPke+8myDljY\/osIPmtYvor5XnvJblhpnmtYvor5XnlKjkvovvvJsg5oqA5pyv77yabGlnaHQgKyB2dWUgKyB3ZWV4IOaUtuiOt++8miDljY\/osIPmsp\/pgJrooajovr7og73lipvlvpfliLDkuoblvojlpKfnmoTmj5Dpq5jvvJsg6L+b5LiA5q2l5o6M5o+h5L+h5omY5Lia5Yqh5qih5Z2X77ya55S15a2Q5ZCI5ZCM77yM5L+h5oGv5oqr6Zyy77yM5a6e5ZCN6K6k6K+B562J77ybIOeGn+aCieS\/oeaJmOeahOS6pOaYk+a1geeoi++8muivt+axguKAlCZndDtUQSZhZ3JhdmU76ZO26IGU5omj5qy+4oCUJmd0O+i\/lOWbnlRBJm5ic3A7PGJyIC8+PC9wPiIsImRlcGFydG1lbnQiOiLnoJTlj5EiLCJza2lsbExhYmVscyI6WyLlkI7nq68iLCLmnI3liqHlmajnq68iXX0sImVkdWNhdGlvbkV4cGVyaWVuY2VzIjpbeyJzY2hvb2xOYW1lIjoi5Y2X5piM5aSn5a2mIiwiZWR1Y2F0aW9uIjoi5pys56eRIiwicHJvZmVzc2lvbmFsIjoi6K6h566X5py656eR5"
        original_content3 = "a2m5LiO5oqA5pyvIiwic3RhcnREYXRlIjoiMjAwNyIsImVuZERhdGUiOiIyMDExIiwic2Nob29sQmFkZ2UiOiJpL2ltYWdlL00wMC9BRC81MS9DZ3AzTzFpMUU3cUFlODZtQUFBdWtBYzhHT1ExNS5qcGVnIiwid2hldGhlckdyYWR1YXRlIjp0cnVlLCJ3aGV0aGVyRnJlc2giOmZhbHNlfV0sImxhdGVzdEVkdWNhdGlvbkV4cGVyaWVuY2UiOnsic2Nob29sTmFtZSI6IuWNl+aYjOWkp+WtpiIsImVkdWNhdGlvbiI6IuacrOenkSIsInByb2Zlc3Npb25hbCI6Iuiuoeeul+acuuenkeWtpuS4juaKgOacryIsInN0YXJ0RGF0ZSI6IjIwMDciLCJlbmREYXRlIjoiMjAxMSIsInNjaG9vbEJhZGdlIjoiaS9pbWFnZS9NMDAvQUQvNTEvQ2dwM08xaTFFN3FBZTg2bUFBQXVrQWM4R09RMTUuanBlZyIsIndoZXRoZXJHcmFkdWF0ZSI6dHJ1ZSwid2hldGhlckZyZXNoIjpmYWxzZX0sImxhdGVzdEVkdUFuZEV4cCI6IlBIUCAmbWlkZG90OyDoh7PlloTnvZHnu5zogqHku73mnInpmZDlhazlj7ggfCDmnKznp5EgJm1pZGRvdDsg5Y2X5piM5aSn5a2mIiwicHJvamVjdEV4cGVyaWVuY2VzIjpbeyJwcm9qZWN0TmFtZSI6Iuezu+e7nyIsInBvc2l0aW9uTmFtZSI6IiIsInN0YXJ0RGF0ZSI6IjIwMTMuMDYiLCJlbmREYXRlIjoiMjAxNi4wMSIsInByb2plY3RSZW1hcmsiOiI8cD7pobnnm67ns7vnu588L3A+IiwiZHV0eVJlbWFyayI6IjxwPueLrOeri+WujOaIkDwvcD4iLCJyZXN1bWVJZCI6Mzk4NjQ2NSwiY3JlYXRlVGltZSI6IjIwMTkwMjE5VDE5MDkyOCswODAwIiwicHJvamVjdFVybCI6IiIsInByb2plY3ROYW1lQW5kUmVtYXJrIjoi57O757ufIn1dLCJleHBlY3RKb2IiOnsiY2l0eSI6IuS4iua1tyIsInBvc2l0aW9uVHlwZSI6IuWFqOiBjCIsInBvc2l0aW9uTmFtZSI6IlBIUCIsInNhbGFyeXMiOiIxNWstMzBrIiwiYWRkRXhwbGFpbiI6IiIsImFycml2YWxUaW1lIjoiM+S4quaciOS7peS4iiIsInN0YXR1cyI6Iumaj+S+v+eci+eciyJ9LCJleHBlY3RKb2JTdHIiOiLkuIrmtbfvvIzlhajogYzvvIzmnIjolqoxNWstMzBr77yMUEhQIiwic29jaWFsQWNjb3VudHMiOltdLCJ1c2VyRGVmaW5lIjp7InRpdGxlTmFtZSI6IuaKgOacr+a4heWNlSIsInRpdGxlQ29udGVudCI6Ijx1bD5cbiA8bGk+54af5oKJZmFzdGNnaeOAgXBocC1mcG3jgII8L2xpPlxuIDxsaT7nhp\/mgonmlbDmja7lupPov57mjqXmsaDjgIFlcG9sbOOAgWVhY2NlbGVyYXRvcuOAgXBjbnRs44CBcmFiYml0bXHjgIFzaWVnZSjmgKfog73ljovlipvmtYvor5Up44CCPC9saT5cbiA8bGk+54af5oKJbWVtY2FjaGXjgIFyZWRpc++8jHJlZGlz55u45YWz6YWN572u5LyY5YyW77yMcmVkaXPlpIfku73jgII8L2xpPlxuIDxsaT7nhp\/mgolNeXNxbO+8jG15aXNhbeOAgWlubm9kYuW8leaTju+8jOWtmOWCqOi\/h+eoi++8jOS4u+S7juWkh+S7veetieOAgjwvbGk+XG4gPGxpPueGn+aCiVRDUOOAgVVEUOOAgXNvY2tldOOAgjwvbGk+XG4gPGxpPueGn+aCiUxpbnV444CBU2hlbGzjgII8L2xpPlxuIDxsaT7nhp\/mgolweXRob27jgIFub2RlanPjgIFqYXZh44CBYW5kcm9pZOOAgjwvbGk+XG4gPGxpPuS6huino0x1YeOAgjwvbGk+XG48L3VsPiIsImNyZWF0ZVRpbWUiOiIyMDE2MDQyNVQwMTQ4MTQrMDgwMCJ9LCJza2lsbEV2YWx1YXRlcyI6W10sIndvcmtTaG93cyI6W10sImFiaWxpdHlMYWJlbHMiOlsi5Liq5Lq66IO95YqbIiwi5rKf6YCa5Y2P6LCD6IO95YqbIl19LCJvcGVuQ29weSI6ZmFsc2UsImRlbGl2ZXJJZCI6MTA5OTk5OTIwNTM0MDcyOTM0NCwibWFyayI6ZmFsc2UsInN0YXR1cyI6IkFVVE9fRklMVEVSIn0sInJvd3MiOltdfX0="

        if environment == 't':
            url = 'http://testing2.common-ats.rpc/atsng/rpc'
        if environment == '':
            url = 'http://common-ats.rpc/atsng/rpc'

        print("15999" + onlyId)
        para = {
            "request": {
                "p": {
                    "position_name": "自动化测试工程师lp",
                    "city_name": "上海",
                    "sourceJid": "",
                    "sourceJidFrom": "1",
                    "deliveryTime": t,
                    "email": "peng.liu1@ifchange.com",
                    "password": "abc123",
                    "vipname": "",
                    "ifchange_position_ids": [6836640],
                    "type": 1,
                    "originalExt": "html",
                    "subject": "lp测123sad费",
                    "content": content,
                    "original_content": original_content1 + original_content2 + original_content3
                },
                "c": "delivery",
                "m": "emailDelivery"
            }
        }
        return json.dumps(para['request'])

    def checkOpSql(self, type, primaryKey):
        sql = "SELECT pk FROM  tob_ats_track.op_record_2019_q@  where  top_id=94211 and type = \"" + str(
            type) + "\"  and pk= \"" + str(primaryKey) + "\" order by id desc   limit 1"

        q = 0
        month = datetime.datetime.now().month
        if month <= 3:
            q = 1
        elif month > 3 & month <= 6:
            q = 2
        elif month > 6 & month <= 9:
            q = 3
        elif month > 9 & month <= 12:
            q = 4
        sql = sql.replace("@", str(q))
        return sql

    def checkAtsSql(self, type1, key, ):
        if str(type1) == "delivery":
            # tob_resumeid超长转char输出
            sql = "SELECT delivery_id,CAST(tob_resume_id AS CHAR)   FROM  tob_ats_5.delivery  where top_id = 94211 and icdc_resume_id = " + str(
                key) + " order by delivery_id desc limit 1"
        elif str(type1) == "delivery_source":
            sql = "SELECT source_id FROM  tob_ats_5.delivery_source  where top_id = 94211 and  tob_resume_id = " + str(
                key) + " order by source_id desc limit 1"
        elif str(type1) == "review_record":
            sql = "SELECT record_id from  tob_ats_5.recruit_review_record AS a LEFT JOIN tob_ats_5.recruit_step as b on a.step_id = b.step_id WHERE b.uid = '94211' and   b.tob_position_id=9634 and tob_resume_id="+str(key)+" ORDER BY record_id desc limit 1;"
        elif str(type1) == "step":
            sql = "SELECT step_id FROM  tob_ats_5.recruit_step  where top_id = 94211 and  stage_id=2 and tob_position_id=9634 and tob_resume_id = " + str(
                key) + " order by step_id desc limit 1"
        elif str(type1)== "employee":
            sql = "SELECT employee_id FROM  tob_ats_5.employee  where top_id = 94211 and  name='lp'  order by employee_id desc limit 1"
        else:
            print("ERROR")
            sql = ""
        return sql

    def reviewPara(self, tob_resume_id, icdc_resume_id, isNewEmployee):
        if isNewEmployee =='1':
            employeeEmail=  str(int(time.time())) + "@qq.com"
        else:
            employeeEmail="peng.liu@ifchange.com"
        request = {
            "employee":[{
            "name":"lp",
            "email":employeeEmail,
            "phone":"",
            "history":1,
            "mark":"0"
            }
            ],
            "candidate":[{
            "tob_resume_id":tob_resume_id,
            "icdc_resume_id":int(icdc_resume_id),
            "tob_position_id":9634
            }
            ],
            "from":"",
            "email_to_interviewer_content":"<p>亲爱的 <a href=\"reviewer_name\">评审官姓名</a>：</p><p>您好，邀请您参加评审，评审信息如下：</p><p><a href=\"candidateInfo\">候选人信息</a></p>",
            "email_to_interviewer_subject":"简历评审-自动化测试工程师lp",
            "sms_to_interviewer":0,
            "stage_type_id":1,
            "stage_id":2}
        return  json.dumps(request)
