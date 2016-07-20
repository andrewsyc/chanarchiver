from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, text
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy import insert
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from datetime import datetime
from sqlalchemy import DateTime

import re
from bs4 import BeautifulSoup
import urllib
import urllib2
import os
import dryscrape
import time

import sys

reload(sys)
sys.setdefaultencoding('utf8')


engine = create_engine('mysql+pymysql://root:magical18'
                               '@localhost/chanarive')


board = 'sci'
# header_html = engine.execute("SELECT header_html FROM header WHERE boardname = {}".format(board))
# print header_html
# thread = ""
# for i in header_html:
#     print i
#     print str(i[0])
#     thread += str(i[0])
#
# thread_to_generate = engine.execute("SELECT post_message FROM sci WHERE threadID = '{}'".format(thread_num))
# for i in thread_to_generate:
#     thread += i[0]





thread_number = engine.execute("SELECT DISTINCT threadID FROM sci ORDER BY threadID DESC")

for i in thread_number:
    thread_num = i[0]
    posts = engine.execute("SELECT position_in_thread, post_message FROM sci WHERE threadID = {} ORDER BY position_in_thread ASC".format(i[0]))
    thread = ""

    header_html = engine.execute("SELECT header_html FROM header WHERE boardname = 'sci'")
    for i in header_html:
        thread += i[0]

    for j in posts:
        # print j[1]
        thread += j[1]

    file = open('/var/www/{}/{}.html'.format(board,thread_num), 'w')
    file.write(thread)
    file.close()
