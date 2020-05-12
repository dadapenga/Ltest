# -*- coding: UTF-8 -*-
#抓取图片

import urllib;
import urllib.request;
import re;


def getHtml(url):
    page = urllib.request.urlopen(url);
    html = page.read();
    return html.decode('UTF-8');


def getImage(html):
    reg = r'http[^\s]*.(?:jpg|png)'  # "http.*?\.png|http.*?\.jpg"  ;#       '"imgUrl": "(http.*?\.jpg)"'
    regli = re.compile(reg);
    reglist = regli.findall(html)
    path = 'D:\\testdir\\'
    x = 0;
    print(reglist)
    print(len(reglist))
    for imageUrL in reglist:
        print(type(imageUrL))
        try:
            print(imageUrL)
            urllib.request.urlretrieve(imageUrL.replace("\\", ""), path + str(x) + '.png')
            x = x + 1
            print(x)
        except:
            print("失败")

html = getHtml("https://news.baidu.com");
print(getImage(html))
