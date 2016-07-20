
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

def md5(board, directory, fname):
    hash_md5 = hashlib.md5()
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + board + '/' + directory + '/' + fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    print hash_md5.hexdigest()
    return hash_md5.hexdigest()

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

boards = ['b','sci','s']


for board in boards:

    catalog_ranker_check.check_catalog(board)


    threads_that_need_to_be_botted = engine.execute("SELECT threadID FROM {}_catalog WHERE bot = 1 LIMIT 100".format(board))
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

        # try:
        rank = 1
        for i in links:
            # Boolean to determine whether media files are in the post
            post_has_media = 0

            # Gets the localhost value of the image
            thumbnail_url = ""
            image_url = ""

            # md5 hashes of files
            thumbnail_md5 = ""
            image_md5 = ""


            items = BeautifulSoup(str(i), "lxml")
            item = items.find("span", attrs={"class": "quote"})

            formatted_message = str(i)

            image_urls = BeautifulSoup(formatted_message, "lxml")


            images = image_urls.find_all("a", attrs={"class": "fileThumb"})

            try:
                for image in images:

                    # If this executes then the post does have media
                    post_has_media = 1
                    thumbnail = BeautifulSoup(str(image), "lxml")
                    thumbnail = thumbnail.find_all("img")
                    urllib.urlretrieve("http:" + image['href'], os.path.dirname(os.path.realpath(__file__)) + '/' + board + '/' + urls[0] + '/' + image['href'].split(board+'/')[1])
                    image_url = image['href'].split(board+'/')[1]
                    image_md5 = md5(board, urls[0], image['href'].split(board+'/')[1])
                    # print os.path.dirname(os.path.realpath(__file__)) + '/' +board + '/' +image['href'].split(board+'/')[1].split('.')[0] + '/' + image['href'].split(board+'/')[1]
                    for thumb in thumbnail:

                        # print thumb['src']  #prints thumbnail url
                        urllib.urlretrieve("http:" + thumb['src'], os.path.dirname(os.path.realpath(__file__)) + '/' + board + '/' + urls[0] + '/' + thumb['src'].split(board+'/')[1])
                        thumbnail_url = thumb['src'].split(board + '/')[1]
                        thumbnail_md5 = md5(board, urls[0], image['href'].split(board+'/')[1])
            except Exception as e:
                print e
                pass


            try:
                formatted_message = formatted_message.replace("//i.4cdn.org/" + board, urls[0])

                image_urls = BeautifulSoup(formatted_message, "lxml")
                to_replace = image_urls.find_all(re.compile("//i.4cdn.org"))
                # print len(to_replace)
                for loc in to_replace:
                    new_link = unicode(loc).replace('//i.4cdn.org', urls[0])
                    image_urls.replace_with(new_link)



                soup = BeautifulSoup(str(image_urls), 'lxml')
                strip_tags = soup.find('div')
                formatted_message = str(strip_tags)
            except Exception as e:
                print e
                pass







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



            if post_has_media == 0:
                query = '''INSERT INTO {0}_mod (threadID, position_in_thread, post_message, moderated, approved) VALUES (%s, %s, %s, %s, %s)'''.format(board)
                # print query
                engine.execute(query, (urls[0], rank, formatted_message, 1, 1))

            elif post_has_media == 1:
                # print "test"
                # print rank
                # print thumbnail_url
                # print image_url

                query = '''INSERT INTO {0}_mod (threadID, position_in_thread, post_message, local_thumbnail, local_image, thumbnail_md5,
                        image_md5, moderated, approved) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''.format(board)
                # print query
                # query = '''INSERT INTO {0}_mod (threadID, position_in_thread, post_message) VALUES (%s, %s, %s)'''.format(board)


                engine.execute(query, (urls[0], rank, formatted_message, thumbnail_url, image_url, thumbnail_md5, image_md5, 0, 0))
                # engine.execute(query, urls[0], rank, formatted_message)

            rank += 1

        # except Exception as e:
        #     print e
        #     pass






    # DELETES any duplicate entries

    query = '''DELETE n1 FROM {0}_mod n1, {0}_mod n2 WHERE n1.id > n2.id AND n1.threadID = n2.threadID AND n1.position_in_thread = n2.position_in_thread'''.format(board)
    result = engine.execute(query)




print time.time() - start