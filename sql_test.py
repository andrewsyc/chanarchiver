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
import dryscrape
import time

start = time.time()






def get_threads(url, board, dir):






    engine = create_engine('mysql+pymysql://root:magical18'
                               '@localhost/chanarive')

    print engine

    # metadata = MetaData()
    # chanarive = Table('b_temp', metadata,
    #     Column('id', Integer(), primary_key=True),
    #     Column('threadID', String()),
    #     Column('position', Integer()),
    #     Column('previous_position', Integer()),
    #
    #     )
    # metadata.create_all(engine)


    # ins = insert('b_temp').values(
    #             # post_id is auto inserted
    #             threadID='324325',
    #             position=4,
    #             previous_position=64,
    #
    #         )

    # insert into database the parsed logic
    # engine.execute("INSERT INTO b_temp (threadID,position,previous_position) VALUES ('2343', 34, 54)")
    # rows = 0
    # item = engine.execute("SELECT * FROM b_temp WHERE threadID = '689718729'")
    # num_rows = engine.execute("SELECT COUNT(*) FROM b_temp")
    # for i in num_rows:
    #     rows = i[0]
    engine.execute("UPDATE b_temp SET remove = 1 WHERE remove = 0")
    engine.execute("UPDATE b_temp SET bot = 0 WHERE bot = 1")
    engine.execute("UPDATE b_temp SET previous_position = current_position")


    # creat a for each loop of all parsed threads
    items = engine.execute("SELECT IF ( EXISTS( SELECT * FROM b_temp WHERE threadID = '{}'), 1, 0)".format('690s617627'))
    # items = engine.execute("SELECT remove FROM b_temp")
    # print len(items)
    for i in items:
         if i[0]:
             # update rank
             print "It exists!"
         else:
             # insert into database
             print "404!"


#     Here delete all items with remove set to 1
#     Here set bot to 1 where current < previous











catalog = "catalog"
prepend = ["boards",]
append = ['b',]

for dir in append:
    for board in prepend:
        print board
        url = "http://{}.4chan.org/{}/{}".format(board, dir, catalog)
        print "This is the directory: " + url
        get_threads(url, board, dir)


end = time.time()
print(end - start)
# thread-689639897
