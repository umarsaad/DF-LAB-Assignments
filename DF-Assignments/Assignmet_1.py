import hashlib
import argparse
import os
import tarfile
import time

parsing=argparse.ArgumentParser()
parsing.add_argument('file')
parsing.add_argument('-b')
out=parsing.parse_args()
source=open(out.file,'rb')
tm =str(time.time())
bytes=b'x00'
evidence=open("compress_image",'wb')
hash_algo=hashlib.sha256()
while bytes:
    bytes=source.read(out.b)
    evidence.write(bytes)
    hash_algo.update(bytes)
hash_algo.update(tm.encode())
print(hash_algo.hexdigest())
source.close()
evidence.close()
compress=tarfile.open('compress_image.tar','w:xz')
compress.add('compress_image')
compress.close()
