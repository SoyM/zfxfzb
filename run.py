# -*- coding: utf-8 -*-

import os

JwUrl = ''

os.system("scrapy crawl score -a JwUrl=%s" % JwUrl)