# coding=utf-8
'''

'''
from __future__ import print_function
import requests
import os, sys, json
from time import time
from google.protobuf import json_format
import codecs
import grpc

sys.path.append('../../../')

from demo_icdcJson import base_json

from multiprocessing import Pool, Queue, Manager

with codecs.open('demo.txt', 'r', 'utf-8-sig') as f1:
    cv_data = json.load(f1)
with codecs.open("evaluation_json.txt", 'r', 'utf-8-sig') as f2:
    eval_data = json.load(f2)
with codecs.open("interview_json.txt", 'r', 'utf-8-sig') as f3:
    inter_data = json.load(f3)
with codecs.open("bei_json.txt", 'r', 'utf-8-sig') as f4:
    bei_data = json.load(f4)
with open("eval.txt", 'rb+') as f5:
    person_type_json = f5.read()
cv_json = json.dumps(cv_data).encode('utf-8')
eval_json = json.dumps(eval_data).encode('utf-8')
interview_json = json.dumps(inter_data).encode('utf-8')
bei_json = json.dumps(bei_data).encode('utf-8')
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
old_profile = base_json('2002')
old_json = json.dumps(json.loads(old_profile)).encode('utf-8')


# print(type(cv_json))
# old_json=json.dumps(test_api_GetProfileRequest.run()).encode('utf-8')
# print(old_json)
def run():  # (num,res_times):
    with open('server.crt', 'rb') as f:
        # with open('server_online.crt','rb') as f:
        gen_certificate = f.read()
    '''CV = 1;INTERVIEW = 2;BEIBOT = 3;EVAL = 4 '''
    # channel = grpc.insecure_channel("10.9.10.32:18012")
    # channel = grpc.insecure_channel("botg.rpc:80")
    # channel = grpc.insecure_channel("testing2.botg.rpc:80")
    creds = grpc.ssl_channel_credentials(gen_certificate)
    # channel = grpc.secure_channel("talent_profile.bot.grpc:51817",creds)
    channel = grpc.secure_channel("talent_profile.testing2.bot.grpc:51817", creds)
    stub = talent_profile_service_pb2_grpc.TalentProfileStub(channel)
    start = time()
    response = stub.GenProfile(
        talent_profile_service_pb2.GenTalentProfileRequest(src_id=2, uuid='', request_type=1, data=cv_json,
                                                           old_profile=b''))
    end = time()
    # including_default_value_fields=True表示展示所有默认值，如果是False表示不展示为空or零的值
    response_dict = json_format.MessageToDict(response, including_default_value_fields=True,
                                              use_integers_for_enums=True,
                                              preserving_proto_field_name=True)
    response_json = json.dumps(response_dict, indent=4, ensure_ascii=False, sort_keys=True)
    # res_times.append(end-start)
    # print('task %s response time : %0.2fs'%(num,(end-start)))
    print(response_json)


# f=open("resultsxujin.txt",'w+')
# f.write(response_json)
# f.close()
# print(json.dumps(response.results).encode('utf-8').decode('unicode_escape'))

def refresh_profile():
    # 更新冰山上的画像
    url_refresh = "https://bot.testing2.ifchange.com/api/center/offline/refresh_profile"
    # print(type(old_profile))
    # print(json.loads(old_profile))
    # print(type(str(cv_json)))
    # print(type(json.dumps(cv_data,ensure_ascii=False)))
    print(type(cv_data))
    print(type(json.loads(old_profile)))
    # json_cv_json=json.dumps(cv_data,ensure_ascii=False)
    # import base64
    # base64_cv_json=base64.b64encode(json_cv_json.encode('utf-8'))
    data = {
        "header": {
            "appid": 20,
            "log_id": "dev",
            "uid": "",
            "uname": "",
            "provider": "dashboard",
            "signid": "",
            "version": "",
            "ip": ""
        },
        "request": {
            "c": "",
            "m": "",
            "p": {
                "src_id": 2,
                "uuid": "1226|2751|1448857521950515227|815|6833900",
                # center.user_products中状态为2的user_id 到dashboard的free_users表中查uuid，就是已经面试过的uuid才可以，整个工程端统一
                "resume": cv_data,
                "talent_profile": json.loads(old_profile),
                "product_ids": []
            }
        }
    }

    res = requests.post(url_refresh, json=data)
    # info=res.json()
    print(res.text)


if __name__ == '__main__':
    # run()#生成画像
    refresh_profile()  # 更新画像
    res_times=[]
    res_times=Manager().list()#共享服务
    p=Pool(20)
    for i in range(1):#用于压测使用，如果单执行填写range(1)
        p.apply_async(run,(i,res_times))
    p.close()
    p.join()
    print('avg times:%s'%(sum(res_times)/len(res_times)))
    print('res_times len:%s'%len(res_times))
    print('QPS/TPS :%s'%(len(res_times)/(sum(res_times)/20)))

