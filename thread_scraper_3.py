
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
import catalog_ranker_check

reload(sys)
sys.setdefaultencoding('utf8')

start = time.time()


base_url = 'http://boards.4chan.org'

engine = create_engine('mysql+pymysql://root:Supermon12'
                                   '@localhost/chanarchive')


# boards = ['a','c','w','m','cgl','cm','n','jp','v','vg','vp','vr','co','g','tv','k',
#           'o','an','tg','sp','asp','sci','his','int','out','toy','i','po','p','ck','ic','wg','mu','fa',
#           '3','gd','diy','wsg','qst','biz','fit','x','lit','adv','lgbt','mlp','news','wsr','b','r9k','pol','soc','s4s',
#           's','hc','hm','h','e','u','d','y','t','hr','gif','aco','r']

boards = ['y','t','hr','gif','aco','r']


for board in boards:

    catalog_ranker_check.check_catalog(board)


    threads_that_need_to_be_botted = engine.execute("SELECT threadID FROM {}_catalog WHERE bot = 1".format(board))
    for urls in threads_that_need_to_be_botted:


        if not os.path.exists(board + '/' + urls[0]):
            os.makedirs(board + '/' + urls[0])




        browser = webdriver.PhantomJS(executable_path='/root/anaconda2/bin/phantomjs') # or add to your PATH
        browser.get('http://boards.4chan.org/{}/thread/{}/'.format(board, urls[0]))
        browser.set_page_load_timeout(3000)


        response = browser.page_source


        # query = '''SELECT COUNT(*) {0}_mod (threadID, position_in_thread, post_message) VALUES (%s, %s, %s)'''.format(board)
        # engine.execute(query, (urls[0], rank, formatted_message))


        # Delete all rows for testing purposes
        # engine.execute("DELETE FROM {}_mod".format(board))

        soup = BeautifulSoup(response.encode('utf-8'), "lxml")

        head = soup.find_all("head")

        links = soup.find_all(id=re.compile("pc"))

        to_thread = str(head)

        # todo download all the

        try:
            rank = 1
            for i in links:
                # print i['id'].split('c')[1]
                items = BeautifulSoup(str(i), "lxml")
                item = items.find("span", attrs={"class": "quote"})
                # to_thread += str(i)
                # insert_statement = 'INSERT INTO sci (threadID, position_in_thread, post_message) VALUES ({}, {}, {})'.format('3453', rank, "message")
                formatted_message = str(i)
                # if isinstance(i, str):
                #     print "ordinary string"
                # elif isinstance(i, unicode):
                image_urls = BeautifulSoup(formatted_message, "lxml")
                # print '\n\n\n' + str(image_urls)

                images = image_urls.find_all("a", attrs={"class": "fileThumb"})

                try:
                    for image in images:
                        # print image['href']  #prints images url
                        thumbnail = BeautifulSoup(str(image), "lxml")
                        thumbnail = thumbnail.find_all("img")
                        urllib.urlretrieve("http:" + image['href'], os.path.dirname(os.path.realpath(__file__)) + '/' + board + '/' + urls[0] + '/' + image['href'].split(board+'/')[1])

                        for thumb in thumbnail:
                            # print thumb['src']  #prints thumbnail url
                            urllib.urlretrieve("http:" + thumb['src'], os.path.dirname(os.path.realpath(__file__)) + '/' + board + '/' + urls[0] + '/' + thumb['src'].split(board+'/')[1])
                except:
                    pass


                try:
                    formatted_message = formatted_message.replace("//i.4cdn.org/" + board, urls[0])

                    image_urls = BeautifulSoup(formatted_message, "lxml")
                    to_replace = image_urls.find_all(re.compile("//i.4cdn.org"))
                    # print len(to_replace)
                    for loc in to_replace:
                        new_link = unicode(loc).replace('//i.4cdn.org', urls[0])
                        image_urls.replace_with(new_link)

                    # print image_urls
                    # formatted_message = str(image_urls)

                    soup = BeautifulSoup(str(image_urls), 'lxml')
                    strip_tags = soup.find('div')
                    formatted_message = str(strip_tags)
                except:
                    pass





                # for image in images:
                #     print image['href']

                #     print "unicode string"
                # else:
                #     print "not a string"

                # unicode_str = str(i)
                # encoded_str = i.encode(encoding='UTF-8',errors='strict')
                # print encoded_str

                # insert_statement = "INSERT INTO sci (threadID, position_in_thread, post_message) VALUES ({}, {}, '{}')".format(threadnumber, rank, encoded_str)
                # engine.execute(text(insert_statement))

                '''
                What this does is counts how many entries from the previous scrape have been entered, that way duplicates are not entered into the
                database.
                '''
                # query = '''SELECT count(position_in_thread) FROM {0}_mod WHERE threadID = {1}'''.format(board, urls[0])
                # reply = engine.execute(query)
                # current_number_replies = 0
                # for total_replies in reply:
                #     current_number_replies = total_replies[0]

                # if total_replies < rank:
                query = '''INSERT INTO {0}_mod (threadID, position_in_thread, post_message) VALUES (%s, %s, %s)'''.format(board)
                engine.execute(query, (urls[0], rank, formatted_message))

                rank += 1

        except:
            pass



        # file = open('/var/www/test.html', 'w')
        # file.write(to_thread)
        # file.close()

        # links =soup.find_all("div", attrs={"class": "thread"})
        # # print str(links)
        # soup = BeautifulSoup(str(links), "lxml")
        # links = soup.find_all("div", attrs={"class": "thread"})
        # print links
        # print len(links)


    # DELETES any duplicate entries
    query = '''DELETE n1 FROM {0}_mod n1, {0}_mod n2 WHERE n1.id > n2.id AND n1.threadID = n2.threadID AND n1.position_in_thread = n2.position_in_thread'''.format(board)
    result = engine.execute(query)


print time.time() - start
import time

import sys
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf8')

start = time.time()


base_url = 'http://boards.4chan.org'

engine = create_engine('mysql+pymysql://root:Supermon12'
                                   '@localhost/chanarchive')


# boards = ['a','c','w','m','cgl','cm','n','jp','v','vg','vp','vr','co','g','tv','k',
#           'o','an','tg','sp','asp','sci','his','int','out','toy','i','po','p','ck','ic','wg','mu','fa',
#           '3','gd','diy','wsg','qst','biz','fit','x','lit','adv','lgbt','mlp','news','wsr','b','r9k','pol','soc','s4s',
#           's','hc','hm','h','e','u','d','y','t','hr','gif','aco','r']

boards = ['tv','k',
          'o','an','tg','sp','asp','sci','his','int','out','toy','i','po','p','ck','ic','wg','mu','fa',
          '3','gd','diy','wsg','qst','biz','fit','x','lit','adv','lgbt','mlp','news','wsr','b','r9k','pol','soc','s4s',
          's','hc','hm','h','e','u','d','y','t','hr','gif','aco','r']


for board in boards:




    threads_that_need_to_be_botted = engine.execute("SELECT threadID FROM {}_catalog WHERE bot = 1".format(board))
    for urls in threads_that_need_to_be_botted:


        if not os.path.exists(board + '/' + urls[0]):
            os.makedirs(board + '/' + urls[0])




        browser = webdriver.PhantomJS(executable_path='/root/anaconda2/bin/phantomjs') # or add to your PATH
        browser.get('http://boards.4chan.org/{}/thread/{}/'.format(board, urls[0]))
        browser.set_page_load_timeout(3000)


        response = browser.page_source


        # query = '''SELECT COUNT(*) {0}_mod (threadID, position_in_thread, post_message) VALUES (%s, %s, %s)'''.format(board)
        # engine.execute(query, (urls[0], rank, formatted_message))


        # Delete all rows for testing purposes
        # engine.execute("DELETE FROM {}_mod".format(board))

        soup = BeautifulSoup(response.encode('utf-8'), "lxml")

        head = soup.find_all("head")

        links = soup.find_all(id=re.compile("pc"))

        to_thread = str(head)

        # todo download all the

        try:
            rank = 1
            for i in links:
                # print i['id'].split('c')[1]
                items = BeautifulSoup(str(i), "lxml")
                item = items.find("span", attrs={"class": "quote"})
                # to_thread += str(i)
                # insert_statement = 'INSERT INTO sci (threadID, position_in_thread, post_message) VALUES ({}, {}, {})'.format('3453', rank, "message")
                formatted_message = str(i)
                # if isinstance(i, str):
                #     print "ordinary string"
                # elif isinstance(i, unicode):
                image_urls = BeautifulSoup(formatted_message, "lxml")
                # print '\n\n\n' + str(image_urls)

                images = image_urls.find_all("a", attrs={"class": "fileThumb"})

                try:
                    for image in images:
                        # print image['href']  #prints images url
                        thumbnail = BeautifulSoup(str(image), "lxml")
                        thumbnail = thumbnail.find_all("img")
                        urllib.urlretrieve("http:" + image['href'], os.path.dirname(os.path.realpath(__file__)) + '/' + board + '/' + urls[0] + '/' + image['href'].split(board+'/')[1])

                        for thumb in thumbnail:
                            # print thumb['src']  #prints thumbnail url
                            urllib.urlretrieve("http:" + thumb['src'], os.path.dirname(os.path.realpath(__file__)) + '/' + board + '/' + urls[0] + '/' + thumb['src'].split(board+'/')[1])
                except:
                    pass


                try:
                    formatted_message = formatted_message.replace("//i.4cdn.org/" + board, urls[0])

                    image_urls = BeautifulSoup(formatted_message, "lxml")
                    to_replace = image_urls.find_all(re.compile("//i.4cdn.org"))
                    # print len(to_replace)
                    for loc in to_replace:
                        new_link = unicode(loc).replace('//i.4cdn.org', urls[0])
                        image_urls.replace_with(new_link)

                    # print image_urls
                    # formatted_message = str(image_urls)

                    soup = BeautifulSoup(str(image_urls), 'lxml')
                    strip_tags = soup.find('div')
                    formatted_message = str(strip_tags)
                except:
                    pass





                # for image in images:
                #     print image['href']

                #     print "unicode string"
                # else:
                #     print "not a string"

                # unicode_str = str(i)
                # encoded_str = i.encode(encoding='UTF-8',errors='strict')
                # print encoded_str

                # insert_statement = "INSERT INTO sci (threadID, position_in_thread, post_message) VALUES ({}, {}, '{}')".format(threadnumber, rank, encoded_str)
                # engine.execute(text(insert_statement))

                '''
                What this does is counts how many entries from the previous scrape have been entered, that way duplicates are not entered into the
                database.
                '''
                # query = '''SELECT count(position_in_thread) FROM {0}_mod WHERE threadID = {1}'''.format(board, urls[0])
                # reply = engine.execute(query)
                # current_number_replies = 0
                # for total_replies in reply:
                #     current_number_replies = total_replies[0]

                # if total_replies < rank:
                query = '''INSERT INTO {0}_mod (threadID, position_in_thread, post_message) VALUES (%s, %s, %s)'''.format(board)
                engine.execute(query, (urls[0], rank, formatted_message))

                rank += 1

        except:
            pass



        # file = open('/var/www/test.html', 'w')
        # file.write(to_thread)
        # file.close()

        # links =soup.find_all("div", attrs={"class": "thread"})
        # # print str(links)
        # soup = BeautifulSoup(str(links), "lxml")
        # links = soup.find_all("div", attrs={"class": "thread"})
        # print links
        # print len(links)


    # DELETES any duplicate entries
    query = '''DELETE n1 FROM {0}_mod n1, {0}_mod n2 WHERE n1.id > n2.id AND n1.threadID = n2.threadID AND n1.position_in_thread = n2.position_in_thread'''.format(board)
    result = engine.execute(query)


print time.time() - start