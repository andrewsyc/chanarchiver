
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from datetime import datetime
from sqlalchemy import DateTime

import re
from bs4 import BeautifulSoup
import urllib
import urllib2
import time

import sys
from selenium import webdriver
import catalog_ranker_check
import hashlib
import os

engine = create_engine('mysql+pymysql://root:Supermon12'
                                   '@localhost/chanarchive')

boards = ['sci']


for board in boards:



    # engine.execute(query)
    # for i in item:
    #     print i[0]

    # items = engine.execute("SELECT * FROM {0}_mod".format(board))
    # for item in items:
        # print item['position_in_thread']

        # query = '''INSERT INTO {0}_archive (threadID, position_in_thread, post_message, local_thumbnail, local_image, thumbnail_md5, image_md5, imgur_thumbnail_url, imgur_image_url, imgur_thumbnail_id, imgur_id,
        #             imgur_thumbnail_deletehash, imgur_deletehash, moderated, approved, dmca, illegal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''.format(board)
        #         # print query
        # engine.execute(query, item['threadID'], item['position_in_thread'], item['post_message'], item['local_thumbnail'], item['local_image'], item['thumbnail_md5'], item['image_md5'], item['imgur_thumbnail_url'], item['imgur_image_url'], item['imgur_thumbnail_id'],
        #                item['imgur_id'], item['imgur_thumbnail_deletehash'], item['imgur_deletehash'], item['moderated'], item['approved'], item['dmca'], item['illegal'])


    # query = '''INSERT INTO {0}_archive (threadID, position_in_thread, post_message, local_thumbnail, local_image, thumbnail_md5, image_md5, imgur_thumbnail_url, imgur_image_url, imgur_thumbnail_id, imgur_id,
    #             imgur_thumbnail_deletehash, imgur_deletehash, moderated, approved, dmca, illegal) SELECT (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) FROM {1}_mod'''.format(board)
    #         # print query
    # engine.execute(query, item['threadID'], item['position_in_thread'], item['post_message'], item['local_thumbnail'], item['local_image'], item['thumbnail_md5'], item['image_md5'], item['imgur_thumbnail_url'], item['imgur_image_url'], item['imgur_thumbnail_id'],
    #                item['imgur_id'], item['imgur_thumbnail_deletehash'], item['imgur_deletehash'], item['moderated'], item['approved'], item['dmca'], item['illegal'])

    # query = '''INSERT INTO {0}_archive (threadID, position_in_thread, post_message, local_thumbnail, local_image, thumbnail_md5, image_md5, imgur_thumbnail_url, imgur_image_url, imgur_thumbnail_id, imgur_id,''' \
    #             '''imgur_thumbnail_deletehash, imgur_deletehash, moderated, approved, dmca, illegal) SELECT threadID, position_in_thread, post_message, local_thumbnail, local_image, thumbnail_md5, image_md5, imgur_thumbnail_url, imgur_image_url, imgur_thumbnail_id, imgur_id,''' \
    #             '''imgur_thumbnail_deletehash, imgur_deletehash, moderated, approved, dmca, illegal) FROM {1}_mod'''.format(board)
            # print query
    # query = '''INSERT INTO {0}_archive SELECT d.* FROM {1}_mod d WHERE approved = 1'''.format(board, board)


    # query = '''INSERT INTO {0}_archive SELECT * FROM {1}_mod WHERE approved = 1'''.format(board, board)
    # engine.execute(query)

    # query = '''DELETE n1 FROM {0}_archive n1, {0}_archive n2 WHERE n1.id > n2.id AND n1.threadID = n2.threadID AND n1.position_in_thread = n2.position_in_thread'''.format(board)
    # result = engine.execute(query)

    # This counts all the rows in the _mod and _archive to make sure there is parity
    # query = '''SELECT count(*) FROM sci_mod'''
    #
    # item = engine.execute(query)
    #
    # for i in item:
    #     print i[0]
    #
    # query = '''SELECT count(*) FROM sci_archive'''
    #
    # item = engine.execute(query)
    # for i in item:
    #     print i[0]



    try:
        query = '''DELETE FROM {0}_archive WHERE moderated = 1 or moderated = 0'''.format(board)
        engine.execute(query)

        query = '''SELECT DISTINCT threadID FROM {0}_mod'''.format(board)

        query = '''DELETE FROM  {0}_mod'''.format(board)
    except Exception as e:
        print e
        pass