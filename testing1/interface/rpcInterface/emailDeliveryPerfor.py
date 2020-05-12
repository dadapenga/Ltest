#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: emailDeliveryPerfor.py
@time: 2019/4/1 15:34
@desc:
'''

import json, time, requests, random, sys, os
from multiprocessing import Queue, Pool, Manager

# 原始简历的
original_content1 = "ZnJvbV9qc29uX2VuY29kZV9yZXN1bHQ6eyJzdGF0ZSI6MSwibWVzc2FnZSI6IuaTjeS9nOaIkOWKnyIsImNvbnRlbnQiOnsiZGF0YSI6eyJwb3NpdGlvbk5hbWUiOiLnvZHnu5zlt6XnqIvluIgiLCJkZWxpdmVyVGltZSI6IjIwMTktMDItMjUgMTk6NDciLCJwb3NpdGlvbklkIjo0NDE2NjA2LCJoYXZlSW50ZXJ2aWV3IjpmYWxzZSwicmVzdW1lVmVyc2lvbiI6IlY0IiwieXVuc3RhdHVzIjoiIiwicmVzdW1lVm8iOnsiaWQiOiI1YzZiZTUwMjE4MjNjZTMzN2JjYjlhOTYiLCJzZXgiOiLnlLciLCJiaXJ0aGRheSI6IjE5ODkuMTAiLCJiaXJ0aFllYXIiOjE5ODksImJpcnRoTW9udGgiOiIxMCIsImJpcnRoRGF0ZSI6IjEiLCJhZ2VOdW0iOjMwLCJ3b3JrWWVhciI6IjblubQiLCJwaG9uZSI6IjE1ODIxNzc1Mjc4IiwiZW1haWwiOiJkYW5tZHJAMTYzLmNvbSIsInN0YXR1cyI6IuaIkeebruWJjeW3suemu+iBjO+8jOWPr+W\/q+mAn+WIsOWylyIsIm15UmVtYXJrIjoiPHVsPiBcbiA8bGk+PHA+Jm5ic3A75pys5Lq65oSP5ZCR55S15ZWG5oiW6auY5bm25Y+R77yM6LSj5Lu75b+D6Z2e5bi45by677yM6ICQ5Yqb5oyB5LmF77yM54Ot54ix5oqA5pyv77yM55qu5a6e44CC5pys5Lq656ym5ZCI56iL5bqP5ZGY54m55b6B5YaF5pWb44CB54G15rS744CB5omn552A44CC54Ot6KG35LqO5oqA5pyv77yM5bSH5bCa56eR5oqA5pS55Y+Y5LiW55WM44CCJm5ic3A7PGJyIC8+PC9wPjwvbGk+XG48L3VsPiIsInJlc3VtZU5hbWUiOiLlvKDmmI7nmoTnroDljoYiLCJuYW1lIjoi5byg5piOIiwibmFtZURlcyI6IiIsImNyZWF0ZVRpbWUiOiIyMDE5MDIxOVQxOTAzNDArMDgwMCIsInVwZGF0ZVRpbWUiOiIyMDE5MDIxOVQxOTA5MjgrMDgwMCIsInJlZnJlc2hUaW1lIjoiMjAxOS0wMi0xOSAxOTowOSIsInBlcmZlY3QiOiIxMTExMDEwMTExMDAwMDAxMTExMDAwMDAxMTEwMDAxMDExMDAxMTExMTAxMSIsImhlYWRQaWMiOiJjb21tb24vaW1hZ2UvcGMvZGVmYXVsdF9ib3lfaGVhZHBpYzMucG5nIiwidXNlcklkIjo0OTA4MTQ1LCJoaWdoZXN0RWR1Y2F0aW9uIjoi5pys56eRIiwib25lV29yZCI6IuWBmuS6i+iupOecn+OAgei0n+i0o++8jOazqOmHjeWboumYn+WQiOS9nOOAgiIsImxpdmVDaXR5Ijoi5LiK5rW3IiwidXNlcklkZW50aXR5IjoyLCJyZXN1bWVJZCI6Mzk4NjQ2NSwicmVzdW1lU2NvcmUiOi0xLCJyZXN1bWVLZXkiOiIiLCJjb21wYW55TmFtZSI6IuS4nOiOnue+juWunOS9syIsIndvcmtFeHBlcmllbmNlcyI6W3siY29tcGFueU5hbWUiOiLoh7PlloTnvZHnu5zogqHku73mnInpmZDlhazlj7giLCJwb3NpdGlvbk5hbWUiOiJQSFAiLCJzdGFydERhdGUiOiIyMDEzLjAzIiwiZW5kRGF0ZSI6IjIwMTYuMDQiLCJjcmVhdGVUaW1lIj"
original_content2 = "oiMjAxNjA0MjVUMDEzNzA2KzA4MDAiLCJ3b3JrQ29udGVudCI6IjxwPiZuYnNwO+S\/oeaJmOWfuue6v+eJiDQuMCDliY3nq6\/lvIDlj5Hlt6XnqIvluIgg5oGS55Sf55S15a2Q6IKh5Lu95pyJ6ZmQ5YWs5Y+4IOS4u+imgei0n+i0o+S7u+WKoe+8miDlj4LkuI7kv6HmiZjkuJrliqHnmoTliLblrprvvIzmlbTlkIjkvJjnp4Dkv6HmiZjlhazlj7jova\/ku7bnmoTnibnngrnvvJsg5Yi25a6a5Z+657q\/54mI5byA5Y+R55qE5Lu75Yqh6KeE5YiS77yM5bm25Y+C5LiO5byA5Y+R77ybIOWNj+iwg+a1i+ivlee8luWGmea1i+ivleeUqOS+i++8myDmioDmnK\/vvJpsaWdodCArIHZ1ZSArIHdlZXgg5pS26I6377yaIOWNj+iwg+ayn+mAmuihqOi+vuiDveWKm+W+l+WIsOS6huW+iOWkp+eahOaPkOmrmO+8myDov5vkuIDmraXmjozmj6Hkv6HmiZjkuJrliqHmqKHlnZfvvJrnlLXlrZDlkIjlkIzvvIzkv6Hmga\/miqvpnLLvvIzlrp7lkI3orqTor4HnrYnvvJsg54af5oKJ5L+h5omY55qE5Lqk5piT5rWB56iL77ya6K+35rGC4oCUJmd0O1RBJmFncmF2ZTvpk7bogZTmiaPmrL7igJQmZ3Q76L+U5ZueVEEmbmJzcDs8YnIgLz48L3A+IiwiZGVwYXJ0bWVudCI6IueglOWPkSIsInNraWxsTGFiZWxzIjpbIuWQjuerryIsIuacjeWKoeWZqOerryJdfV0sImxhdGVzdFdvcmtFeHBlcmllbmNlIjp7ImNvbXBhbnlOYW1lIjoi6Iez5ZaE572R57uc6IKh5Lu95pyJ6ZmQ5YWs5Y+4IiwicG9zaXRpb25OYW1lIjoiUEhQIiwic3RhcnREYXRlIjoiMjAxMy4wMyIsImVuZERhdGUiOiIyMDE2LjA0IiwiY3JlYXRlVGltZSI6IjIwMTYwNDI1VDAxMzcwNiswODAwIiwid29ya0NvbnRlbnQiOiI8cD4mbmJzcDvkv6HmiZjln7rnur\/niYg0LjAg5YmN56uv5byA5Y+R5bel56iL5biIIOaBkueUn+eUteWtkOiCoeS7veaciemZkOWFrOWPuCDkuLvopoHotJ\/otKPku7vliqHvvJog5Y+C5LiO5L+h5omY5Lia5Yqh55qE5Yi25a6a77yM5pW05ZCI5LyY56eA5L+h5omY5YWs5Y+46L2v5Lu255qE54m554K577ybIOWItuWumuWfuue6v+eJiOW8gOWPkeeahOS7u+WKoeinhOWIku+8jOW5tuWPguS4juW8gOWPke+8myDljY\/osIPmtYvor5XnvJblhpnmtYvor5XnlKjkvovvvJsg5oqA5pyv77yabGlnaHQgKyB2dWUgKyB3ZWV4IOaUtuiOt++8miDljY\/osIPmsp\/pgJrooajovr7og73lipvlvpfliLDkuoblvojlpKfnmoTmj5Dpq5jvvJsg6L+b5LiA5q2l5o6M5o+h5L+h5omY5Lia5Yqh5qih5Z2X77ya55S15a2Q5ZCI5ZCM77yM5L+h5oGv5oqr6Zyy77yM5a6e5ZCN6K6k6K+B562J77ybIOeGn+aCieS\/oeaJmOeahOS6pOaYk+a1geeoi++8muivt+axguKAlCZndDtUQSZhZ3JhdmU76ZO26IGU5omj5qy+4oCUJmd0O+i\/lOWbnlRBJm5ic3A7PGJyIC8+PC9wPiIsImRlcGFydG1lbnQiOiLnoJTlj5EiLCJza2lsbExhYmVscyI6WyLlkI7nq68iLCLmnI3liqHlmajnq68iXX0sImVkdWNhdGlvbkV4cGVyaWVuY2VzIjpbeyJzY2hvb2xOYW1lIjoi5Y2X5piM5aSn5a2mIiwiZWR1Y2F0aW9uIjoi5pys56eRIiwicHJvZmVzc2lvbmFsIjoi6K6h566X5py656eR5"
original_content3 = "a2m5LiO5oqA5pyvIiwic3RhcnREYXRlIjoiMjAwNyIsImVuZERhdGUiOiIyMDExIiwic2Nob29sQmFkZ2UiOiJpL2ltYWdlL00wMC9BRC81MS9DZ3AzTzFpMUU3cUFlODZtQUFBdWtBYzhHT1ExNS5qcGVnIiwid2hldGhlckdyYWR1YXRlIjp0cnVlLCJ3aGV0aGVyRnJlc2giOmZhbHNlfV0sImxhdGVzdEVkdWNhdGlvbkV4cGVyaWVuY2UiOnsic2Nob29sTmFtZSI6IuWNl+aYjOWkp+WtpiIsImVkdWNhdGlvbiI6IuacrOenkSIsInByb2Zlc3Npb25hbCI6Iuiuoeeul+acuuenkeWtpuS4juaKgOacryIsInN0YXJ0RGF0ZSI6IjIwMDciLCJlbmREYXRlIjoiMjAxMSIsInNjaG9vbEJhZGdlIjoiaS9pbWFnZS9NMDAvQUQvNTEvQ2dwM08xaTFFN3FBZTg2bUFBQXVrQWM4R09RMTUuanBlZyIsIndoZXRoZXJHcmFkdWF0ZSI6dHJ1ZSwid2hldGhlckZyZXNoIjpmYWxzZX0sImxhdGVzdEVkdUFuZEV4cCI6IlBIUCAmbWlkZG90OyDoh7PlloTnvZHnu5zogqHku73mnInpmZDlhazlj7ggfCDmnKznp5EgJm1pZGRvdDsg5Y2X5piM5aSn5a2mIiwicHJvamVjdEV4cGVyaWVuY2VzIjpbeyJwcm9qZWN0TmFtZSI6Iuezu+e7nyIsInBvc2l0aW9uTmFtZSI6IiIsInN0YXJ0RGF0ZSI6IjIwMTMuMDYiLCJlbmREYXRlIjoiMjAxNi4wMSIsInByb2plY3RSZW1hcmsiOiI8cD7pobnnm67ns7vnu588L3A+IiwiZHV0eVJlbWFyayI6IjxwPueLrOeri+WujOaIkDwvcD4iLCJyZXN1bWVJZCI6Mzk4NjQ2NSwiY3JlYXRlVGltZSI6IjIwMTkwMjE5VDE5MDkyOCswODAwIiwicHJvamVjdFVybCI6IiIsInByb2plY3ROYW1lQW5kUmVtYXJrIjoi57O757ufIn1dLCJleHBlY3RKb2IiOnsiY2l0eSI6IuS4iua1tyIsInBvc2l0aW9uVHlwZSI6IuWFqOiBjCIsInBvc2l0aW9uTmFtZSI6IlBIUCIsInNhbGFyeXMiOiIxNWstMzBrIiwiYWRkRXhwbGFpbiI6IiIsImFycml2YWxUaW1lIjoiM+S4quaciOS7peS4iiIsInN0YXR1cyI6Iumaj+S+v+eci+eciyJ9LCJleHBlY3RKb2JTdHIiOiLkuIrmtbfvvIzlhajogYzvvIzmnIjolqoxNWstMzBr77yMUEhQIiwic29jaWFsQWNjb3VudHMiOltdLCJ1c2VyRGVmaW5lIjp7InRpdGxlTmFtZSI6IuaKgOacr+a4heWNlSIsInRpdGxlQ29udGVudCI6Ijx1bD5cbiA8bGk+54af5oKJZmFzdGNnaeOAgXBocC1mcG3jgII8L2xpPlxuIDxsaT7nhp\/mgonmlbDmja7lupPov57mjqXmsaDjgIFlcG9sbOOAgWVhY2NlbGVyYXRvcuOAgXBjbnRs44CBcmFiYml0bXHjgIFzaWVnZSjmgKfog73ljovlipvmtYvor5Up44CCPC9saT5cbiA8bGk+54af5oKJbWVtY2FjaGXjgIFyZWRpc++8jHJlZGlz55u45YWz6YWN572u5LyY5YyW77yMcmVkaXPlpIfku73jgII8L2xpPlxuIDxsaT7nhp\/mgolNeXNxbO+8jG15aXNhbeOAgWlubm9kYuW8leaTju+8jOWtmOWCqOi\/h+eoi++8jOS4u+S7juWkh+S7veetieOAgjwvbGk+XG4gPGxpPueGn+aCiVRDUOOAgVVEUOOAgXNvY2tldOOAgjwvbGk+XG4gPGxpPueGn+aCiUxpbnV444CBU2hlbGzjgII8L2xpPlxuIDxsaT7nhp\/mgolweXRob27jgIFub2RlanPjgIFqYXZh44CBYW5kcm9pZOOAgjwvbGk+XG4gPGxpPuS6huino0x1YeOAgjwvbGk+XG48L3VsPiIsImNyZWF0ZVRpbWUiOiIyMDE2MDQyNVQwMTQ4MTQrMDgwMCJ9LCJza2lsbEV2YWx1YXRlcyI6W10sIndvcmtTaG93cyI6W10sImFiaWxpdHlMYWJlbHMiOlsi5Liq5Lq66IO95YqbIiwi5rKf6YCa5Y2P6LCD6IO95YqbIl19LCJvcGVuQ29weSI6ZmFsc2UsImRlbGl2ZXJJZCI6MTA5OTk5OTIwNTM0MDcyOTM0NCwibWFyayI6ZmFsc2UsInN0YXR1cyI6IkFVVE9fRklMVEVSIn0sInJvd3MiOltdfX0="
environment_type = 't'

positionsName = ['', '', '']


class tob_rpc():
    def __init__(self):
        pass

    def tob_delivery_inner(self):
        url = '/atsng/rpc'
        api = rpcAPI(environment_type, url)
        # 接口参数表示
        # $p = [
        # 'position_name' => '网络工程师', // 职位名称 必填
        # 'city_name' => '', // 城市名称
        # 'sourceJidFrom' => 11, // 投递渠道 必填
        # 'deliveryTime' => false, // 投递时间 必填
        # 'email' => 'baolong.yang@ifchange.com', // 邮箱用户名 必填   baolong.yang@ifchange.com是非白名单    ying.zhang@ifchange.com是白名单用户
        # 'password' => 'abc123', // 邮箱密码 必填
        # 'subject' => '网络工程师：张明的简历（来自拉勾）', // 邮件主题 必填
        # 'originalExt' => 'html', // 简历原件格式 必填
        # 'content' => '', // 简历格式化数据 必填
        # 'original_content' => '', // 简历原件格式 必填
        # 'ifchange_position_ids' => '',//基础数据职位ID，兼容参数    以后可能会没有
        # ];
        api.params = {
            "request": {
                "p": {
                    "position_name": "lp测试职位3",
                    "city_name": "上海",
                    "sourceJid": "",
                    "sourceJidFrom": "19",
                    "deliveryTime": 1551877541,
                    "email": "ying.zhang@ifchange.com",
                    "password": "Zhang2016",
                    "vipname": "",
                    "ifchange_position_ids": [6836640],
                    "type": 1,
                    "originalExt": "docx",
                    "subject": "lp测123sad费",
                    "content": content,
                    # "content":source+contact+basic+work+project+education,
                    "original_content": original_content1 + original_content2 + original_content3
                    # "original_content": oridoc_1 + oridoc_2 + oridoc_3 + oridoc_4 + oridoc_5 + oridoc_6 + oridoc_7 + oridoc_8 + oridoc_9
                },
                "c": "delivery",
                "m": "emailDelivery"
            },
            "header": {
                "provider": "testing_aide",
                "uid": 1226
            }
        }
        result = api.do_test()


randint = random.randint(555555, 999999)
content = "{\"source\":{\"src\":\"20\",\"src_no\":\"5c6be5021823ce337bcb9a96\"},\"contact\":{\"phone\":\"15999990021\",\"email\":\"lptestingemail21@163.com\"},\"basic\":{\"resume_name\":\"lp\\u90ae\\u4ef6\\u6d4b\\u8bd521\\u7684\\u7b80\\u5386\",\"name\":\"lp\\u90ae\\u4ef6\\u6d4b\\u8bd521\",\"gender\":\"M\",\"work_experience\":\"6\",\"birth\":\"1989\\u5e7410\\u6708\",\"age\":\"30\",\"expect_type\":\"\\u5168\\u804c\",\"address\":\"105\",\"expect_position_name\":\"PHP\",\"current_status\":\"1\",\"updated_at\":\"2019-02-19 19:09:00\",\"expect_city_ids\":\"105\",\"expect_salary_from\":\"15\",\"expect_salary_to\":\"30\"}}"


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

def testcase(i):
    time.sleep(0.5)
    print(++i)


if __name__ == "__main__":
    obj = tob_rpc()
    resTimes= []
    resTimes=Manager().list()
    p = Pool(20)
    for i in range(1,20):
        p.apply_async(testcase(i),(i,resTimes))
    p.close()
    p.join()
    print(resTimes)
    print('avg times:%s'%(sum(resTimes)/len(resTimes)))
    print('resTimes len:%s'%len(resTimes))
    print('QPS/TPS:%s'%(len(resTimes)/(sum(resTimes)/20 )))