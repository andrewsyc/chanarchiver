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

start = time.time()

engine = create_engine('mysql+pymysql://root:Supermon12'
                                   '@localhost/chanarchive')


# boards = ['a','c','w','m','cgl','cm','n','jp','v','vg','vp','vr','co','g','tv','k',
#           'o','an','tg','sp','asp','sci','his','int','out','toy','i','po','p','ck','ic','wg','mu','fa',
#           '3','gd','diy','wsg','qst','biz','fit','x','lit','adv','lgbt','mlp','news','wsr','b','r9k','pol','soc','s4s',
#           's','hc','hm','h','e','u','d','y','t','hr','gif','aco','r']

# boards = ['b']

# removed w and m for initial scrape


for board in boards:

  try:
    query = "CREATE TABLE `{0}_catalog` (" \
      "`id` int(11) unsigned NOT NULL AUTO_INCREMENT," \
      "`threadID` varchar(100) NOT NULL," \
      "`current_position` int(11) DEFAULT NULL," \
      "`previous_position` int(11) DEFAULT '255'," \
      "`bot` tinyint(1) DEFAULT '1'," \
      "`remove` tinyint(1) DEFAULT '0'," \
      "PRIMARY KEY (`id`)" \
    ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;".format(board)

    engine.execute(query)

  except:
    pass



  try:
    query = "CREATE TABLE `{0}_mod` (" \
    "`id` int(20) unsigned NOT NULL AUTO_INCREMENT," \
    "`threadID` varchar(100) NOT NULL," \
    "`position_in_thread` varchar(20) DEFAULT NULL," \
    "`post_message` blob," \
    "PRIMARY KEY (`id`)" \
    ") ENGINE=InnoDB AUTO_INCREMENT=8203 DEFAULT CHARSET=latin1;".format(board)

    engine.execute(query)

  except:
    pass