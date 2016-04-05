#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This modle will help you put your local file to 
QiNiu cloud storage, I use it to share files and
pictures in my blog.
"""
import argparse
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

def getBucket(uploadAuth):
    """
    Get the bucket object.
    """
    return BucketManager(uploadAuth)

def checkFile(bucket, filePath, bucketName):
    """
    Check the file path is right and if it is exist in the bucket.
    """
    if not os.path.exists(filePath):
        print "Wrong file path: %s" % (filePath)
        return False

    ret, info = bucket.stat(bucketName, filePath)
    if ret:
        print "File exists in Qiniu cloud: %s" % (filePath)
    return ret == None

def check_conf(conf_file):
    """
    Check the configure file is existed.
    """
    if not os.path.exists(conf_file):
        print "ERROR: Cannot find configure file."
        print "Please create configure file: %s" % (conf_file)
        print "[DEFAULT]"
        print "default_bucket_name ="
        print "access_key ="
        print "secret_key ="
        print "domain ="

        sys.exit(1)

def main():
    # Check the configure file
    check_conf(conf_file)

    # Read configure file
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file)

    parser = argparse.ArgumentParser(prog="quupload",
            description="This is a tool to upload file to Qiniu cloud.")
    parser.add_argument("file", 
                        metavar="filepath",
                        help="Specify a file to upload to Qiniu cloud.")
    parser.add_argument("-b", "--bucket",
                        default=cf.get("DEFAULT", "default_bucket_name"),
                        help="A bucket under your Qiniu account.")
    parser.add_argument("-a", "--access-key",
                        default=cf.get("DEFAULT", "access_key"),
                        help="Your access key.")
    parser.add_argument("-s", "--secret-key",
                        default=cf.get("DEFAULT", "secret_key"),
                        help="Your secret key.")
    parser.add_argument("-d", "--domain",
                        default=cf.get("DEFAULT", "domain"),
                        help="The domain of your Qiniu account to share \
                              the file you upload to Qiniu cloud.")
    args = parser.parse_args()

    filePath = args.file
    uploadAuth = getAuth(args.access_key, args.secret_key)
    bucket = getBucket(uploadAuth)
    if checkFile(bucket, filePath, args.bucket):
        uploadFile(args.bucket, args.file, uploadAuth, args.domain)

if __name__ == '__main__':
    main()
