
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

from bs4 import BeautifulSoup
import urllib
import urllib2
import os
import time
from time import sleep


start = time.time()

from selenium import webdriver






# boards = ['a','c','w','m','cgl','cm','n','jp','v','vg','vp','vr','co','g','tv','k',
#           'o','an','tg','sp','asp','sci','his','int','out','toy','i','po','p','ck','ic','wg','mu','fa',
#           '3','gd','diy','wsg','qst','biz','fit','x','lit','adv','lgbt','mlp','news','wsr','b','r9k','pol','soc','s4s',
#           's','hc','hm','h','e','u','d','y','t','hr','gif','aco','r']


def check_catalog(board):
    boards = [board]

    for board in boards:


        browser = webdriver.PhantomJS(executable_path='/root/anaconda2/bin/phantomjs') # or add to your PATH
        browser.get("http://boards.4chan.org/{}/catalog".format(board))
        browser.set_page_load_timeout(3000)


        # element = browser.find_element_by_name('html')
        response = browser.page_source



        print "Hello everyone!"


        engine = create_engine('mysql+pymysql://root:Supermon12'
                                   '@localhost/chanarchive')

        soup = BeautifulSoup(response.encode('utf-8'), "lxml")
        # print soup
        # print "This is soup:" + str(soup)

        links =soup.find_all("div", attrs={"class": "thread"})
        # print str(links)
        # print len(links)
        # for l in links:
        #     print l
        soup = BeautifulSoup(str(links), "lxml")
        links = soup.find_all("div", attrs={"class": "thread"})
        # print links
        # print len(links)
        threadList = []

        rank = 1 #Set initial rank to 1 for counting
        engine.execute("UPDATE {}_catalog SET remove = 1 WHERE remove = 0".format(board))
        engine.execute("UPDATE {}_catalog SET bot = 0 WHERE bot = 1".format(board))
        engine.execute("UPDATE {}_catalog SET previous_position = current_position".format(board))
        engine.execute("UPDATE {}_catalog SET current_position = 255".format(board))

        for i in links:
            threadList.append(i['id'].split('-')[1])
            thread_num = i['id'].split('-')[1]


            # creat a for each loop of all parsed threads
            thread_in_db = engine.execute("SELECT IF ( EXISTS( SELECT * FROM {}_catalog WHERE threadID = '{}'), 1, 0)".format(board,thread_num))
            # items = engine.execute("SELECT remove FROM b_catalog")
            # print len(items)
            for i in thread_in_db:
                if i[0]: #If this is true 1
                     # update rank
                    # engine.execute("UPDATE {}_catalog SET previous_position = current_position".format(board))
                    engine.execute("UPDATE {}_catalog SET current_position = {}, remove = 0 WHERE threadID = {}".format(board,rank, thread_num))
                    print "It exists!"
                else:
                    engine.execute("INSERT INTO {}_catalog (threadID,current_position, remove) VALUES ({}, {}, {})".format(board,thread_num, rank, 1))

                    print "404!"


            # Update rank
            rank += 1

        # engine.execute("DELETE from {}_catalog WHERE remove = 1".format(board))

        engine.execute("UPDATE {}_catalog SET bot = 1 WHERE current_position < previous_position".format(board))
        engine.execute("DELETE FROM {}_catalog WHERE remove = 1 AND bot = 0 AND current_position = 255".format(board))
        print rank








