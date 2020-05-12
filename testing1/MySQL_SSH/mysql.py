#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: mysql.py
@time: 2019/4/11 16:16
@desc:
'''
import pymysql


class mysqlCon():
    #进行线上tob库的链接8.140的3307这里是外网数据库地址
    #head是列名
    def excuteSql(self,sql,db1='tobusiness',head=True):
        db = pymysql.connect(
             host="211.148.28.36",
            port=9100,
            user="tuser",
            password="tu7319m",
            db=db1,
            charset="utf8"
        )
        data = []  # 返回数据
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            colName= []  #列名
            index = cursor.description   #字段信息
            for i in index:
                colName.append(i[0])
            i = cursor.rowcount  #多行的计数
            #是否加head
            if head:
                data.append(colName)

            for j in cursor.fetchall():
                print(j)
                data.append(j)
        except Exception as e:
            print(e)
        finally:
            db.close()
            print("sql查询结束")
        return data


if __name__=='__main__':
    sql = "SELECT * FROM `email_bind_archive` WHERE uid = 94417 AND  email = 'peng.liu@ifchange.com' ; "
    obj = mysqlCon()
    result = obj.excuteSql(sql)
    for i in range(0,len(result)):
        print(result[i])