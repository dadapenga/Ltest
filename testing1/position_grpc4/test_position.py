#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: test_position.py
@time: 2019/1/12 16:54
@desc:
'''

import grpc
import service_pb2_grpc, service_pb2
import random
import profileData
import time
import json
from google.protobuf import json_format

random1 = random.randint(88888888, 99999999)
print(random1)


# 生成一级维度画像
def firstProfile(env="test"):
    # channel = grpc.insecure_channel("testing2.botg.rpc:80")     这是没有加证书的调用  #192.168.1.174:63121    testing2.botg.rpc:80
    url=''
    if env=='test':
        with open('server.crt', 'rb') as f:
            root_cert = f.read()
        url='position_profile.testing2.bot.grpc:51812'
    elif env =='prod':
        with open('server(xs).crt','rb') as f:
            root_cert=f.read()
        url='position_profile.bot.grpc:51812'
    creds = grpc.ssl_channel_credentials(root_cert)
    channel = grpc.secure_channel(url,
                                  creds)  # port:51812  测试环境position_profile.testing2.bot.grpc   开发环境   position_profile.dev.bot.grpc
    stub = service_pb2_grpc.PositionProfileStub(channel)
    # // 来源ID-标记业务端
    # int32 src_id = 1;
    # // 业务端自生成的UUID
    # string uuid = 2;
    # // 筛选项-职能
    # string job_func = 3;
    # // 筛选项-地区
    # int32 plc_id = 4;
    # // 筛选项-工作年限
    # nlpPositionProfile.WorkDuraType work_dura = 5;
    # // JD 可选项
    # nlpPositionProfile.JobDescription jd = 6;
    # start =time.clock()
    response = stub.GenAxis1Profile(
        service_pb2.GenAxis1PositionProfileRequest(src_id=99, uuid='lp' + str(random1), work_dura=3, job_func='java架构师',
                                                   plc_id=1000105, jd=profileData.jdJAVAjiagoushi))
    response_dict = json_format.MessageToDict(response.results, including_default_value_fields=False,
                                              use_integers_for_enums=True, preserving_proto_field_name=True)
    response_json = json.dumps(response_dict, indent=4, ensure_ascii=False, sort_keys=True)
    # print(time.clock()-start)
    print(response_json)


# 修复一级维度画像
def fixFirstProfile(env="test"):
    # channel = grpc.insecure_channel("testing2.botg.rpc:80")
    url=''
    if env=='test':
        with open('server.crt', 'rb') as f:
            root_cert = f.read()
        url='position_profile.testing2.bot.grpc:51812'
    elif env =='prod':
        with open('server(xs).crt','rb') as f:
            root_cert=f.read()
        url='position_profile.bot.grpc:51812'
    creds = grpc.ssl_channel_credentials(root_cert)
    channel = grpc.secure_channel(url,
                                  creds)  # port:51812  测试环境position_profile.testing2.bot.grpc   开发环境   position_profile.dev.bot.grpc
    stub = service_pb2_grpc.PositionProfileStub(channel)
    # // 来源ID-标记业务端
    # int32 src_id = 1;
    # // 业务端自生成的UUID
    # string uuid = 2;
    # // 一级维度画像-修正项-全量覆盖
    # profile.Axis1Profile axis1_profile = 3;
    response = stub.FixAxis1Profile(
        service_pb2.FixAxis1PositionProfileRequest(src_id=99, uuid="lp92540613", axis1_profile={}))
    response_dict = json_format.MessageToDict(response.results, including_default_value_fields=False,
                                              use_integers_for_enums=True, preserving_proto_field_name=True)
    response_json = json.dumps(response_dict, indent=4, ensure_ascii=False, sort_keys=True)
    print(response_json)
    # print(reponse)


# 产生二、三级维度画像
def genFullProfile(env="test"):
    # channel = grpc.insecure_channel("testing2.botg.rpc:80")
    url=''
    if env=='test':
        with open('server.crt', 'rb') as f:
            root_cert = f.read()
        url='position_profile.testing2.bot.grpc:51812'
    elif env =='prod':
        with open('server(xs).crt','rb') as f:
            root_cert=f.read()
        url='position_profile.bot.grpc:51812'
    creds = grpc.ssl_channel_credentials(root_cert)
    channel = grpc.secure_channel(url,
                                  creds)  # port:51812  测试环境position_profile.testing2.bot.grpc   开发环境   position_profile.dev.bot.grpc
    stub = service_pb2_grpc.PositionProfileStub(channel)
    # // 来源ID-标记业务端
    # int32 src_id = 1;
    # // 业务端自生成的UUID
    # string uuid = 2;
    start = time.clock()
    response = stub.GenFullProfile(service_pb2.GenFullPositionProfileRequest(src_id=99, uuid='lp92540613'))
    print(time.clock() - start)
    response_dict = json_format.MessageToDict(response.results, including_default_value_fields=False,
                                              use_integers_for_enums=True, preserving_proto_field_name=True)
    response_json = json.dumps(response_dict, indent=4, ensure_ascii=False, sort_keys=True)
    print(response_json)
    # print(reponse)


# 一次性产生全量画像
def allProfile(env="test"):
    # channel = grpc.insecure_channel("testing2.botg.rpc:80")  #192.168.1.174:63121    testing2.botg.rpc:80
    url=''
    if env=='test':
        with open('server.crt', 'rb') as f:
            root_cert = f.read()
        url='position_profile.testing2.bot.grpc:51812'
    elif env =='prod':
        with open('server(xs).crt','rb') as f:
            root_cert=f.read()
        url='position_profile.bot.grpc:51812'
    creds = grpc.ssl_channel_credentials(root_cert)
    channel = grpc.secure_channel(url,
                                  creds)  # port:51812  测试环境position_profile.testing2.bot.grpc   开发环境   position_profile.dev.bot.grpc
    # stub = service_pb2_grpc.PositionProfileStub(channel)
    stub = service_pb2_grpc.PositionProfileStub(channel)
    # // 来源ID-标记业务端
    # int32 src_id = 1;
    # // 业务端自生成的UUID
    # string uuid = 2;
    # // 筛选项-职能
    # string job_func = 3;
    # // 筛选项-地区
    # int32 plc_id = 4;
    # // 筛选项-工作年限
    # nlpPositionProfile.WorkDuraType work_dura = 5;
    # // JD 可选项
    # nlpPositionProfile.JobDescription jd = 6;
    start = time.clock()
    response = stub.GenProfile(
        service_pb2.GenPositionProfileRequest(src_id=99, uuid='lp' + str(random1), job_func='java架构师', work_dura=3,
                                              plc_id=1000105, jd=profileData.jdJAVAjiagoushi))
    print(time.clock() - start)
    response_dict = json_format.MessageToDict(response.results, including_default_value_fields=False,
                                              use_integers_for_enums=True, preserving_proto_field_name=True)
    response_json = json.dumps(response_dict, indent=4, ensure_ascii=False, sort_keys=True)
    print(response_json)
    # print(response)


# 获取历史画像
def getProfile(env="test"):
    # channel = grpc.insecure_channel("192.168.1.174:63121")  #testing2.botg.rpc:80
    url=''
    if env=='test':
        with open('server.crt', 'rb') as f:
            root_cert = f.read()
        url='position_profile.testing2.bot.grpc:51812'
    elif env =='prod':
        with open('server(xs).crt','rb') as f:
            root_cert=f.read()
        url='position_profile.bot.grpc:51812'
    creds = grpc.ssl_channel_credentials(root_cert)
    channel = grpc.secure_channel(url,
                                  creds)  # port:51812  测试环境position_profile.testing2.bot.grpc   开发环境   position_profile.dev.bot.grpc
    stub = service_pb2_grpc.PositionProfileStub(channel)
    # // 来源ID-标记业务端
    # int32 src_id = 1;
    # // 业务端自生成的UUID
    # repeated string uuids = 2;
    response = stub.GetProfile(service_pb2.GetPositionProfileRequest(src_id=99, uuids=["lp92540613", "lp91239964"]))
    response_dict = json_format.MessageToDict(response.results, including_default_value_fields=False,
                                              use_integers_for_enums=True, preserving_proto_field_name=True)
    response_json = json.dumps(response_dict, indent=4, ensure_ascii=False, sort_keys=True)
    print(response_json)
    # print(response)


if __name__ == '__main__':
    allProfile()
