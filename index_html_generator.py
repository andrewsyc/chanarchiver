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
# import dryscrape.dryscrape.dryscrape
import time

import sys

reload(sys)
sys.setdefaultencoding('utf8')





'''

This creates an html index of all the files

'''


engine = create_engine('mysql+pymysql://root:magical18'
                               '@localhost/chanarive')




thread = "8166911"
board = 'sci'

# Get the header html
header_html = engine.execute("SELECT header_html FROM header WHERE boardname = 'index'")
for i in header_html:
    thread += i[0] # this only adds the header once

# Gets the distinct threads
thread_number = engine.execute("SELECT DISTINCT threadID FROM sci ORDER BY threadID DESC")

# Goes through each seperate post
for num in thread_number:
    thread_num = num[0]

    count_in_thread = engine.execute("SELECT COUNT(*) FROM sci WHERE threadID = {}".format(num[0]))
    count_pos = 0
    for i in count_in_thread:
        count_pos = i[0]

    # If thread has more than 5 posts in it, this will only make the last 5 posts appear in the preview of the thread
    if count_pos > 5:
        count_pos = count_pos - 5
        # print count_pos
        # print "SELECT position_in_thread, post_message FROM sci WHERE threadID = {} AND (position_in_thread = 1 OR position_in_thread > {}) ORDER BY position_in_thread ASC".format(num[0], count_pos)
        posts = engine.execute("SELECT position_in_thread, post_message FROM sci WHERE threadID = {} AND (position_in_thread = 1 OR position_in_thread > {}) ORDER BY position_in_thread ASC".format(num[0], count_pos))
    else:
        # If thread has 5 or less posts, this prints out all the posts in the preview.
        posts = engine.execute("SELECT position_in_thread, post_message FROM sci WHERE threadID = {}  ORDER BY position_in_thread ASC".format(i[0]))


    # Get the posts

    # for j in posts:
    #     print j[1]
    #
    #     thread += j[1]


if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/' +board):
        os.makedirs(os.path.dirname(os.path.realpath(__file__)) + '/' +board)

    file = open(os.path.dirname(os.path.realpath(__file__)) + '/' +board + '/' + thread_num + '.html'.format(board,thread_num), 'w')
    file.write(thread)
    file.close()

