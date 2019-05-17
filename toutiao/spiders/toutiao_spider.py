# @Time : 2019/5/17 10:03
# @Author : 2273360936@qq.com
# @FileName : toutiao_spider.py
# @GitHub : https://github.com/liulichao1/toutiao
from scrapy import Request
from scrapy.spiders import Spider
from selenium import webdriver
from toutiao.items import ToutiaoItem#导入Item模块

class ToutiaoSpider(Spider):
    name = "toutiao"


    def __init__(self):
        self.driver = webdriver.Chrome()


    def start_requests(self):
        url = "https://www.toutiao.com/ch/news_hot/"
        yield Request(url)


    def parse(self, response):
        item = ToutiaoItem()
        list_selector = response.xpath("//div[@class='wcommonFeed']/ul/li")
        for li in list_selector:
            try:
                # 标题
                title = li.xpath(".//a[@class='link title']/text()").extract()
                # 去除空格
                title = title[0].strip(" ")
                # 来源
                source = li.xpath(".//a[@class='lbtn source']/text()").extract()
                # 去除点号和全角空格
                source = source[0].strip("⋅").strip(" ")
                # 评论数
                comment = li.xpath(".//a[@class='lbtn comment']/text()")
                # 去除文字及空格
                comment = comment.re("(.*?)评论")[0]
                comment = "".join(comment.split())  # 去除空格：&nbsp
                item["title"] = title  # 标题
                item["source"] = source  # 来源
                item["comment"] = comment  # 评论数
                yield item
            except:
                continue

