#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: wssTest.py
@time: 2020/2/24 16:28
@desc:
'''

import  json,time
from websocket import  create_connection
from ws4py.client.threadedclient  import WebSocketClient

url = 'wss://candidate_bot.testing2.ifchange.com/websocket'
firstJsonMess = {"session_id": "30zaz9ek8zi", "domain": "https://m-qddf.zhaogong.testing2.cheng95.com", "token": "",
                 "bot_id": 1, "task_id": "441", "bot_type": "1", "position_id": "441", "request_type": "REQUEST_EXAM",
                 "request": {"url": "/bot/information/441", "task_id": "441", "bot_id": 1, "scene": "1.1",
                             "method": "get", "body": {"task_id": "441", "bot_id": 1, "scene": "1.1", "method": "get",
                                                       "session_id": "30zaz9ek8zi",
                                                       "domain": "https://m-qddf.zhaogong.testing2.cheng95.com",
                                                       "token": "", "bot_type": "1", "position_id": "441",
                                                       "open_id": ""}},
                 "fe_cookies": "SERVERID=1; _pk_testcookie..undefined=1; _pk_testcookie.m-qddf.zhaogong.testing2.cheng95.com.05b9=1; user_type=delivery; bole_id=0; recommend_id=0; _pk_ses.m-qddf.zhaogong.testing2.cheng95.com.05b9=1; _pk_id.m-qddf.zhaogong.testing2.cheng95.com.05b9=751988b5e4a5c795.1582513374.2.1582531488.1582530839.",
                 "scene": "1.1"}
firstMess = json.dumps(firstJsonMess)  # 字典转json字符串传递参数，文本参数

#create_connection进行连接
# while True:
#     time.sleep(2)
#     try:
#         ws = create_connection(url)
#         print(ws)
#         ws.send(firstMess)
#         result = ws.recv()  #返回json字符串
#         #result = json.loads(result)   json 字符串转dict字典用来数据处理
#         print(result)
#         ws.close
#         break
#     except Exception as e:
#         print("exception ", format(e))
#         continue




ws =None
try:
    ws=WebSocketClient(url,protocols=['chat'])
    ws.connect()
    # ws.run_forever()
    ws.send(firstMess)
    print()
except Exception as e:
    print(e)
    ws.close()



