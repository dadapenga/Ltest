#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: base64Decode.py
@time: 2019/4/17 14:35
@desc:
'''

import  base64,os

class base64T():
    def decodeBase64(self,):
        with open("1.txt",'rb') as  f:
            str1 = f.read()
        image = base64.b64decode(str1)
        file = open('test.png','wb')
        file.write(image)
        file.close()

    def ToBase64(self,file,txt):
        with open(file, 'rb') as fileObj:
            image_data = fileObj.read()
            base64_data = base64.b64encode(image_data)
            fout = open(txt, 'w')
            fout.write(base64_data.decode())
            fout.close()
if __name__ == '__main__':
     baseTest= base64T()
     # baseTest.decodeBase64()
     baseTest.ToBase64("English.doc","english.txt",)



