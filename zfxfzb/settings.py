# -*- coding: utf-8 -*-

# Scrapy settings for zfxfzb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zfxfzb'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

SPIDER_MODULES = ['zfxfzb.spiders']
NEWSPIDER_MODULE = 'zfxfzb.spiders'


ITEM_PIPELINES = {
    'zfxfzb.pipelines.MyprojectPipeline': 400,
}

# 数据库配置
MYSQL_DB = "wechat"
MYSQL_HOST = "127.0.0.1"
MYSQL_USER = ""
MYSQL_PSW = ""
