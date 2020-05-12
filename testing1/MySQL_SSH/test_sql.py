#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: test_sql.py
@time: 2019/2/21 15:56
@desc:
'''
import pymysql
from sshtunnel import SSHTunnelForwarder
import paramiko
import psycopg2

# server = SSHTunnelForwarder(
#     ssh_address_or_host = ('192.168.1.249', 22),
#     ssh_username = 'liupeng',
#     ssh_password = 'y8V9scNi5PWfGt0u',
#     remote_bind_address = ('10.9.10.6', 3307)
# )
# mysql_config = {
#     'user': 'tuser',
#     'passwd': 'tu7319m',
#     'host': '10.9.10.6',
#     'port': 3307,
#     'db': 'dashboard'
# }
#
# #启动隧道服务
# server.start()
#
# #连接数据库
# connect =pymysql.connect(**mysql_config)
# cursor = connect.cursor()
#
# #查询并打印数据
# cursor.execute('SELECT * from ssc_login_demo ORDER BY id DESC')
# print(cursor.fetchall())
# ------------------------------------------------------------
# pkey = paramiko.RSAKey.from_private_key_file('D:\\navicat\\liupeng.pem',password='y8V9scNi5PWfGt0u')
# ssh = paramiko.SSHClient()
# ssh.connect(hostname='192.168.1.249',
#             port=22,
#             username='liupeng',
#             pkey=pkey)
#
# mysql_config = {
#     'user': 'tuser',
#     'passwd': 'tu7319m',
#     'host': '10.9.10.6',
#     'port': 3307,
#     'db': 'dashboard'
# }
#
# #连接数据库
# connect =pymysql.connect(**mysql_config)
# cursor = connect.cursor()
#
# #查询并打印数据
# cursor.execute('SELECT * from ssc_login_demo ORDER BY id DESC')
# print(cursor.fetchall())
#
# ssh.close()
# ------------------------------------------------------------

private_key = paramiko.RSAKey.from_private_key_file('D:\\navicat\\liupeng.pem',password='y8V9scNi5PWfGt0u')
server = SSHTunnelForwarder(
    ssh_address_or_host = ('192.168.1.249', 22),
    ssh_username = 'liupeng',
    ssh_pkey=private_key,
    # ssh_password = 'y8V9scNi5PWfGt0u',
    remote_bind_address=('10.9.10.6',3307)
)
server.start()


try:
    #连接数据库
    connect =psycopg2.connect(database= 'dashboard',
                              user= 'tuser',
                              password= 'tu7319m',
                              host= '10.9.10.6',
                              port=3307)
    cursor = connect.cursor()

    #查询并打印数据
    cursor.execute('select * from ssc_login_demo ORDER BY id DESC')
    print(cursor.fetchall())

finally:
    server.close()



