from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from os import path
from os import makedirs
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
import time

import sys
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf8')

start = time.time()


base_url = 'http://boards.4chan.org'

engine = create_engine('mysql+pymysql://root:Supermon12'
                                   '@localhost/chanarchive')


boards = ['sci']


for board in boards:

    # DELETES any duplicate entries
    query = '''DELETE n1 FROM {0}_mod n1, {0}_mod n2 WHERE n1.id > n2.id AND n1.threadID = n2.threadID AND n1.position_in_thread = n2.position_in_thread'''.format(board)
    result = engine.execute(query)

    query = '''SELECT count(position_in_thread) FROM {0}_mod WHERE threadID = 8189766'''.format(board)
    result = engine.execute(query)

    for i in result:
        print i[0]

    query = '''SELECT post_message FROM {0}_mod WHERE threadID = 8180660'''.format(board)
    result = engine.execute(query)
    # #
    # for i in result:
    #     soup = BeautifulSoup(str(i[0]), 'lxml')
    #     item = soup.find_all('div')
    #     for i in item:
    #         print str(item) + '\n\n\n'


        # Delete all rows for testing purposes
        # engine.execute("DELETE FROM {}_mod".format(board))




print time.time() - start