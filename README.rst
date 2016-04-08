qnupload
===========================

Install
---------------------------
This Tools can help you to upload your file to QiNiu cloud storage.
You can install this easily,

    python setup.py install

Also can install it via pip:

    pip install qnupload

Help
---------------------------
And you can get help message by run:

    qnupload -h

Configuration
---------------------------
Add some basic configuration items in 

    /etc/qnupload/qnupload.conf

[DEFAULT]
# If you do not specify the bucket name in command line,
# it will use default_bucket_name as the default value.
#
# default_bucket_name = Bucket1

# Create the access key and secret key on QiNiu account and
# qnupload will use them to get the upload token.
#
# access_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# secret_key = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

# Set the domain for bucket to share the file uploaded to
# Qiniu cloud storage, you can get the value from settings
# of bucket on Qiniu.
# If you have serveral buckets, you can add them one by one.
#
# [Bucket1]
# domain = domain1
#
# [Bucket2]
# domain = domain2

Basic operation
---------------------------
After set the bucket, access key and secret key, then you can upload
file with qnupload:

    qnupload File_Path

If you have several buckets in the configuration, but you want upload
the file to a *non default* bucket, you can use `-b`:

    qnupload File_path -b another_bucket

You can choose several files or directories one time:

    qnupload File1 File2 Dir1 Dir2 -b another_bucket
