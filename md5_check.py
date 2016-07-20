import hashlib
import os

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(os.path.dirname(os.path.realpath(__file__)) + '/b/695099613/' + fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()



# statinfo = os.stat('1468795860645.jpg')
# print statinfo.st_size
# f = open(fileName)
# while not endOfFile:
#     f.read(128)

for i in range(1, 500):
    print md5('1468795860645.jpg')



