# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScoreItem(Item):
    courseid = Field()
    studentid = Field()
    examscore = Field()
    coursename = Field()
    dailyscore = Field()
    finalscore = Field()
    realname = Field()


class TorrentItem(Item):
    url = Field()
    name = Field()
    description = Field()
    size = Field()
