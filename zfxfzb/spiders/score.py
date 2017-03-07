# -*- coding: utf-8 -*-
import re
from ..items import ScoreItem
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider


class MininovaSpider(CrawlSpider):
    name = 'score'
    

    def __init__(self, JwUrl=None, *args, **kwargs):
        self.JwUrl =JwUrl
        if JwUrl:
            self.start_urls = [JwUrl+'/excel/']
        else:
            print'\033[1;31;40m请输入链接\033[0m'
            return

    def parse_item(self, response):
        item = ScoreItem()
        score = response.body.decode('GBK')
        kc = u'(?<=>课程名称|选课课号：).*?(?=</)'
        kc = re.findall(re.compile(kc), score)
        if len(kc) == 2:
            item['coursename'] = kc[0][1:]
            item['courseid'] = kc[1]
        else:
            item['coursename'] = None
            item['courseid'] = kc[0]

        data = Selector(text=score).xpath("//tr")
        for td in data.extract():
            row = Selector(text=td).xpath("//td/text()").extract()
            if row and len(row) == 9 and row[1][-2].isdigit():
                item['studentid'] = row[1]
                item['realname'] = row[2]
                item['dailyscore'] = row[3]
                item['examscore'] = row[5]
                item['finalscore'] = row[7]
                yield item

    def parse(self, response):
        scorefile = open("score.log", "rw+")
        scorelog=scorefile.read()
        lines = response.xpath(
            '//a/@href').re("/excel/\d{19}.xls|/excel/.*html")
        if scorelog:
            StartEcho = False
        else:
            StartEcho = True
        for line in lines:
            if StartEcho:
                #print line
                yield Request(self.JwUrl+line, callback=self.parse_item)
            if line in scorelog:
                StartEcho = True
                
        scorefile.write(line+'\n')
        scorefile.close()
