#!/usr/bin/python
# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth
from qiniu import put_file
from qiniu import BucketManager

import os
import sys 
import qiniu.config

#print q.private_download_url

def getAuth():
    access_key = "自己的access_key"
    secret_key = "自己的secret_key"
    
    auth = Auth(access_key, secret_key)
    
    return auth

def isFileExist(bucketName, filePath):
    query = getAuth()
    bucket = BucketManager(query)
    ret,info = bucket.stat(bucketName, filePath)
    if ret == None:
        return False
    else:
        return True

def upload_file(bucketName, filePath):
    fileName = os.path.basename(filePath)
    # 设置分享连接，比如http://7xqb88.com1.z0.glb.clouddn.com/
    # 分享后访问http://7xqb88.com1.z0.glb.clouddn.com/filename即可
    prelink = "Change your own prelink"

    if isFileExist(bucketName, fileName):
        print "File %s is exist, cannot upload the same file!" % fileName
    else:
        auth = getAuth()
        upload_token = auth.upload_token(bucketName)
        ret, resp = qiniu.put_file(upload_token, fileName, filePath)
        print "Upload file: %s" % filePath
        print "Link: %s" % (prelink + fileName)


if len(sys.argv)>2:
    bucketName = sys.argv[2]
else:
    bucketName = "blog"

fileName = "%s" % sys.argv[1]
upload_file(bucketName, fileName)
