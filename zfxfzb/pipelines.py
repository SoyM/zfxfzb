# -*- coding: utf-8 -*-

import MySQLdb
from scrapy.conf import settings


class MyprojectPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PSW'],
            db=settings['MYSQL_DB'],
            host=settings['MYSQL_HOST'],
            charset="utf8",
            use_unicode=True)
        self.cursor = self.conn.cursor()
        # 清空表：
        # self.cursor.execute("truncate table score;")
        # self.conn.commit()

    def process_item(self, item, spider):
        insert_sql = "insert into score (studentid, courseid, coursename, dailyscore, examscore, finalscore) VALUE ('%s', '%s', '%s', '%s', '%s', '%s');"
        update_sql = "update score set coursename='%s',dailyscore='%s',examscore='%s',finalscore='%s' where studentid='%s' and courseid='%s';"
        try:
            self.cursor.execute(insert_sql % (item['studentid'], item['courseid'], item['coursename'],
                                              item['dailyscore'], item['examscore'], item['finalscore']))
            self.conn.commit()
        except MySQLdb.Error, e:
            self.cursor.execute(update_sql % (item['coursename'], item['dailyscore'], item['examscore'],
                                              item['finalscore'], item['studentid'], item['courseid']))
        return item
