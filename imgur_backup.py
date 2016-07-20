from sqlalchemy.ext.automap import automap_base

Base = automap_base()
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import engine

Base = automap_base()
import time
import sys
from imgurpython import ImgurClient
import unirest
import os

client_id = '999ee789e084f2e'
client_secret = '0657e39557991653a45accdef5a16130491ff45a'

client = ImgurClient(client_id, client_secret)

reload(sys)
sys.setdefaultencoding('utf8')

start = time.time()

boards = ['sci']

engine = create_engine('mysql+pymysql://root:Supermon12'
                       '@localhost/chanarchive')


# This will run through the database and simple delete all images that are marked as dmca or illegal
def delete():
    '''
    Delete images
    '''


    to_delete = engine.execute("SELECT * FROM sci_mod")




    for row in to_delete:
        if (row['dmca'] == 1 or row['illegal'] == 1) and (row['imgur_thumbnail_url'] is not None or row['imgur_image_url'] is not None):
        # client.delete_image(img)
        # # These code snippets use an open-source library.
        # These code snippets use an open-source library. http://unirest.io/python
            response = unirest.delete("https://imgur-apiv3.p.mashape.com/3/image/{}".format(row['imgur_deletehash']),
                                      headers={
                "X-Mashape-Key": "y4mVnnNiZBmshBb9s7rh4DSw6K53p1T5SDujsnxxEUEvw62m4L",
                "Authorization": "Client-ID 999ee789e084f2e",
                "Accept": "text/plain"
              }
            )
            print response.body['status']

            if response.body['status'] == 200:
                print "was successful"
            # engine.execute("DELETE FROM imgur WHERE deletehash = {}".format(img[0]))
            # query = '''DELETE FROM imgur WHERE deletehash = %s'''
            # engine.execute(query, (img[0]))


def upload(image_name, board):
    # This will upload the file
    query_string = '''SELECT * FROM {0}_mod WHERE local_thumbnail = %s'''.format(board)
    row = engine.execute(query_string, image_name)
    # print query_string
    # print image_name

    for item in row:
        # necessary variables
        threadID = item['threadID']
        thumbnail = item['local_thumbnail']
        image = item['local_image']

        directory_thumb = '/' + board + '/' + threadID + '/' + thumbnail
        directory_image = '/' + board + '/' + threadID + '/' + image



        """
        Upload the thumbnail
        """
        # try:
            # These code snippets use an open-source library.
        response = unirest.post("https://imgur-apiv3.p.mashape.com/3/{}".format(directory_thumb),
          headers={
            "X-Mashape-Key": "y4mVnnNiZBmshBb9s7rh4DSw6K53p1T5SDujsnxxEUEvw62m4L",
            "Authorization": "Client-ID 999ee789e084f2e",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
          },
          params={
            "image": "<required>"
          }
        )
        #
        print response.body['data']['id']
        print response.body['data']['link']
        print response.body['data']['deletehash']
        #
        try:
            image_thumbnail_id = response.body['data']['id']
            imgur_thumbnail_url = response.body['data']['link']
            deletehash = response.body['data']['deletehash']

            query_string = '''UPDATE {0}_mod set imgur_thumbnail_id = %s, imgur_thumbnail_url = %s, imgur_thumbnail_deletehash = %s WHERE local_thumbnail = %s'''.format(board)
            engine.execute(query_string, image_thumbnail_id, imgur_thumbnail_url, deletehash, image_name)
        except Exception as e:
            print e
            pass

        # except:
        #     pass

        """
        Upload the main image
        """

        try:
            response = unirest.post("https://imgur-apiv3.p.mashape.com/3/{}".format(directory_image),
              headers={
                "X-Mashape-Key": "y4mVnnNiZBmshBb9s7rh4DSw6K53p1T5SDujsnxxEUEvw62m4L",
                "Authorization": "Client-ID 999ee789e084f2e",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
              },
              params={
                "image": "<required>"
              }
            )
            #
            print response.body['data']['id']
            print response.body['data']['link']
            print response.body['data']['deletehash']
            #
            # try:
            imgur_image_id = response.body['data']['id']
            imgur_image_url = response.body['data']['link']
            deletehash = response.body['data']['deletehash']

            query_string = '''UPDATE {0}_mod set imgur_id = %s, imgur_image_url = %s, imgur_deletehash = %s WHERE local_thumbnail = %s'''.format(board)
            engine.execute(query_string, imgur_image_id, imgur_image_url, deletehash, image_name)
        except Exception as e:
            print e
            pass









for board in boards:
    # Runs through and determines if a row either needs an upload of an image or a deletion
    board_rows = engine.execute("SELECT * FROM {0}_mod".format(board))

    for img in board_rows:
        # print "another row"

        if (img['moderated'] == 1 and img['approved'] == 1) and img['imgur_thumbnail_url'] is None and img['local_thumbnail'] is not None:
            print img['local_thumbnail']
            # print "Upload the images and update the database"
            upload(img['local_thumbnail'], board)

        # delete()

    # Runs through entire database for any deletables
    # delete()
