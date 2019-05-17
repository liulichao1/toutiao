# @Time : 2019/5/17 10:20
# @Author : 2273360936@qq.com
# @FileName : start.py
# @GitHub : https://github.com/liulichao1/toutiao
from scrapy import cmdline

cmdline.execute("scrapy crawl toutiao -o toutiao.csv".split())