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

Choose a bucket as default:

    default_bucket_name = Bucket1

Set the access key and secret key, can get them from Qiniu Cloud

    access_key = your_access_key

    secret_key = your_secret_key

Set domain for each bucket, the domain can get form the bucket setting
on your Qiniu account

    [Bucket1]

    domain = domain1
    
    [Bucket2]

    domain = domain2

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
