# -*- coding: utf-8 -*-

import os

JwUrl = 'http://xxx.xxx.xxx.xxx'

os.system("scrapy crawl score -a JwUrl=%s" % JwUrl)
