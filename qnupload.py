#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This modle will help you put your local file to 
QiNiu cloud storage, I use it to share files and
pictures in my blog.
"""
import ConfigParser
import os
import sys 
import qiniu.config

from qiniu import Auth
from qiniu import put_file
from qiniu import BucketManager

conf_file = "/etc/qnupload/qnupload.conf"

def getAuth(accessKey, secretKey):
    """
    Get the auth object by access key and secret key.
    """
    auth = Auth(accessKey, secretKey)
    
    return auth

def uploadFile(bucketName, filePath, auth, domain):
    """
    Upload file to your bucket on qiniu server. 
    """
    fileName = os.path.basename(filePath)

    up_token = auth.upload_token(bucketName)
    ret, resp = qiniu.put_file(up_token, fileName, filePath)
    if ret:
        print "Upload file: %s" % filePath
        print "Link: %s" % (domain + fileName)
    else:
        print "Failed to upload file."

def getBucket(bucketName, uploadAuth):
    """
    Get the bucket object.
    """
    return BucketManager(uploadAuth)

def checkFile(bucket, filePath):
    """
    Check the file path is right and if it is exist in the bucket.
    """
    if not os.path.exists(filePath):
        print "Wrong file path: %s" % (filePath)
        return False

    ret, info = bucket.stat(bucketName, filePath)
    return ret == None

def usage():
    print "usage: qnupload fileName [bucket name]"

if __name__ == '__main__':
    if len(sys.argv)==1:
        print "ERROR: Please specify a file to upload."
        usage()
        sys.exit(1)

    if len(sys.argv)>3:
        print "ERROR: Too many  parameters."
        usage()
        sys.exit(1)
    
    # Check the configure file
    if not os.path.exists(conf_file):
        print "ERROR: Cannot find configure file."
        sys.exit(1)

    # Read configure file
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file)
    accessKey = cf.get("DEFAULT", "access_key")
    secretKey = cf.get("DEFAULT", "secret_key")
    domain = cf.get("DEFAULT", "domain")
    if len(sys.argv)==3:
        bucketName = sys.argv[2]
    else:
        bucketName = cf.get("DEFAULT", "default_bucket_name")

    filePath = sys.argv[1]
    uploadAuth = getAuth(accessKey, secretKey)
    bucket = getBucket(bucketName, uploadAuth)
    if checkFile(bucket, filePath):
        uploadFile(bucketName, filePath, uploadAuth, domain)
