# -*- coding: utf-8 -*-
import requests
import chardet
from parsel import Selector

def getVIP(webSite):
    url = "http://www.vipfenxiang.com/"+webSite+"/"
    page = requests.get(url)
    response = page.content
    iChardet = response.encoding if hasattr(response,'encoding') else chardet.detect(response)['encoding']
    content = response.decode(iChardet,"ignore")
    url = Selector(text=content).xpath('//article/header/h2/a/@href').extract_first()

    page = requests.get(url)
    response = page.content
    iChardet = response.encoding if hasattr(response,'encoding') else chardet.detect(response)['encoding']
    content = response.decode(iChardet,"ignore")
    data = Selector(text=content).xpath('//span[@style="color: #339966;"]/text()').extract()
    for i in data:
        print i


def getVIP_xunlei(webSite):
    url = "http://www.vipfenxiang.com/"+webSite+"/"
    page = requests.get(url)
    response = page.content
    iChardet = response.encoding if hasattr(response,'encoding') else chardet.detect(response)['encoding']
    content = response.decode(iChardet,"ignore")
    url = Selector(text=content).xpath('//article/header/h2/a/@href').extract_first()

    page = requests.get(url)
    response = page.content
    iChardet = response.encoding if hasattr(response,'encoding') else chardet.detect(response)['encoding']
    content = response.decode(iChardet,"ignore")
    data = Selector(text=content).xpath(u'//*[contains(text(),"迅雷vip账号")]/text()').extract()
    for i in data:
        print i


if __name__ == '__main__':
    print("==========优酷==========")
    getVIP("youku")
    print("==========爱奇艺==========")
    getVIP("aiqiyi")
    print("==========迅雷==========")
    getVIP_xunlei("xunlei")
