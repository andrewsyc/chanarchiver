from imgurpython import ImgurClient
import unirest
import os
import base64
import os
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
Base = automap_base()
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

client_id = '67d854ceaa5af4c'
client_secret = 'f632dc2515c06e87c0be56f2377479901a8cf5aa'

client = ImgurClient(client_id, client_secret)


name = client.credits
# print client.get_account_images('andrewsyc')
# print client.credits
print name

engine = create_engine('mysql+pymysql://root:magical18'
                                   '@localhost/imgur')

engine.connect()
'''
Upload images
'''

# images = os.listdir("images")
# for image in images:
#   print image
#   with open(os.path.dirname(os.path.realpath(__file__)) + '/images/' + image, "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#   # These code snippets use an open-source library.
#   # These code snippets use an open-source library.
#   response = unirest.post("https://imgur-apiv3.p.mashape.com/3/image",
#     headers={
#       "X-Mashape-Key": "huYA3ztRaxmshy95Mcj4dTmVrMTHp1iQ858jsn3jpASEst4dig",
#       "Authorization": "Client-ID 67d854ceaa5af4c",
#       "Content-Type": "application/x-www-form-urlencoded",
#       "Accept": "application/json"
#     },
#     params={
#       "image": open(os.path.dirname(os.path.realpath(__file__)) + '/images/' + image, mode='r')
#     }
#   )
#
#   # print response.body['data']['id']
#   # print response.body['data']['link']
#   # print response.body['data']['deletehash']
#
#   try:
#     image_id = response.body['data']['id']
#     url = response.body['data']['link']
#     deletehash = response.body['data']['deletehash']
#
#     print image_id + " " + url + " " + deletehash
#
#   # engine.execute("INSERT INTO imgur (id, url, deletehash) VALUES ({}, {}, {})".format(response.body['data']['id'], response.body['data']['link']), response.body['data']['deletehash'])
#   # engine.execute("INSERT INTO imgur (id, url, deletehash) VALUES ({}, {}, {})".format(image_id, url, deletehash))
#
#
#     query = '''INSERT INTO imgur (id, url, deletehash) VALUES (%s, %s, %s)'''
#     engine.execute(query, (image_id, url, deletehash))
#   except:
#     print "There was an error"
#     pass


'''
'''

# images = os.listdir("images")
# for image in images:
#   print image
#   with open(os.path.dirname(os.path.realpath(__file__)) + '/images/' + image, "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#   # These code snippets use an open-source library.
#   # These code snippets use an open-source library.
#   response = unirest.post("https://imgur-apiv3.p.mashape.com/3/image",
#     headers={
#       "X-Mashape-Key": "huYA3ztRaxmshy95Mcj4dTmVrMTHp1iQ858jsn3jpASEst4dig",
#       "Authorization": "Client-ID 67d854ceaa5af4c",
#       "Content-Type": "application/x-www-form-urlencoded",
#       "Accept": "application/json"
#     },
#     params={
#       "image": open(os.path.dirname(os.path.realpath(__file__)) + '/images/' + image, mode='r')
#     }
#   )
#
#   print response.body




# print response.code
# print response.headers
# print response.body
# print response.raw_body

# 3nNpeJh


'''
Delete images
'''

# to_delete = ["692LfMR1HKotuic","nbxl2ZAcOTO2eoz", "nrsNcrYqUV0A9rH"]
to_delete = engine.execute("SELECT deletehash FROM imgur")
for img in to_delete:
  # client.delete_image(img)
# # These code snippets use an open-source library.
  # These code snippets use an open-source library. http://unirest.io/python
  response = unirest.delete("https://imgur-apiv3.p.mashape.com/3/image/{}".format(img[0]),
    headers={
      "X-Mashape-Key": "huYA3ztRaxmshy95Mcj4dTmVrMTHp1iQ858jsn3jpASEst4dig",
      "Authorization": "Client-ID 67d854ceaa5af4c",
      "Accept": "text/plain"
    }
  )
  print response.body['status']

  if response.body['status'] == 200:
    # engine.execute("DELETE FROM imgur WHERE deletehash = {}".format(img[0]))
    query = '''DELETE FROM imgur WHERE deletehash = %s'''
    engine.execute(query, (img[0]))




'''
'''


# These code snippets use an open-source library.
# response = unirest.get("https://imgur-apiv3.p.mashape.com/3/account/andrewsyc/images/count",
#   headers={
#     "X-Mashape-Key": "huYA3ztRaxmshy95Mcj4dTmVrMTHp1iQ858jsn3jpASEst4dig",
#     "Authorization": "Client-ID 90c416dd63dda31",
#     "Accept": "application/json"
#   }
# )
#
#   # These code snippets use an open-source library.
# response = unirest.get("https://imgur-apiv3.p.mashape.com/3/account/andrewsyc/images/ids",
#   headers={
#     "X-Mashape-Key": "huYA3ztRaxmshy95Mcj4dTmVrMTHp1iQ858jsn3jpASEst4dig",
#     "Authorization": "Client-ID 67d854ceaa5af4c",
#     "Accept": "application/json"
#   }
# )
#
# print response.body['data']

# for i in response.body['data']:
#   print i
#   # These code snippets use an open-source library.
#   response = unirest.delete("https://imgur-apiv3.p.mashape.com/3/image/{}".format(i),
#     headers={
#       "X-Mashape-Key": "huYA3ztRaxmshy95Mcj4dTmVrMTHp1iQ858jsn3jpASEst4dig",
#       "Authorization": "Client-ID 90c416dd63dda31",
#       "Accept": "text/plain"
#     }
#   )
  # print response


# print response.body