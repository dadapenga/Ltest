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

random1 = random.randint(88888888,99999999)
print(random1)
# 生成一级维度画像
def firstProfile():
    channel = grpc.insecure_channel("192.168.1.174:63121")   #192.168.1.174:63121    testing2.botg.rpc:80
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
    reponse = stub.GenAxis1Profile(service_pb2.GenAxis1PositionProfileRequest(src_id=99, uuid='lp' + str(random1), job_func='软件工程师', plc_id=1000105,jd={}))
    print(reponse)

#修复一级维度画像
def fixFirstProfile():
    channel = grpc.insecure_channel("testing2.botg.rpc:80")
    stub = service_pb2_grpc.PositionProfileStub(channel)
    # // 来源ID-标记业务端
    # int32 src_id = 1;
    # // 业务端自生成的UUID
    # string uuid = 2;
    # // 一级维度画像-修正项-全量覆盖
    # profile.Axis1Profile axis1_profile = 3;
    reponse  = stub.FixAxis1Profile(service_pb2.FixAxis1PositionProfileRequest())
    print(reponse)

# 产生二、三级维度画像
def genFullProfile():
    channel = grpc.insecure_channel("testing2.botg.rpc:80")
    stub = service_pb2_grpc.PositionProfileStub(channel)
    # // 来源ID-标记业务端
    # int32 src_id = 1;
    # // 业务端自生成的UUID
    # string uuid = 2;
    reponse = stub.GenFullProfile(service_pb2.GenFullProfileRequest())
    print(reponse)

# 一次性产生全量画像
def allProfile():
    channel = grpc.insecure_channel("192.168.1.174:63121")  #192.168.1.174:63121    testing2.botg.rpc:80
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
    dic= {"description":"1. 计算机相关专业本科以上学历，拥有3年以上端游或手游开发经验","requirement":"1. 基于cocos2dx开发手游客户端框架"}
    response = stub.GenProfile(
        service_pb2.GenPositionProfileRequest(src_id=99, uuid='lp' + str(random1), job_func='软件工程师', plc_id=1000105, jd=dic))
    print(response)

# 获取历史画像
def getProfile():
    channel = grpc.insecure_channel("192.168.1.174:63121")  #testing2.botg.rpc:80
    stub = service_pb2_grpc.PositionProfileStub(channel)
    # // 来源ID-标记业务端
    # int32 src_id = 1;
    # // 业务端自生成的UUID
    # repeated string uuids = 2;
    reponse = stub.GetProfile(service_pb2.GetPositionProfileRequest(src_id=1,uuids = ["111"]))
    print(reponse)



if __name__ == '__main__':
    allProfile()
