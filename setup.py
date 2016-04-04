#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(name = 'qnupload',
      version = VERSION,
      description = 'Tool to upload file to Qiniu cloud',
      keywords = 'python qnupload terminal',
      author = 'cheneydc',
      author_email = 'cheneydc@gmail.com',
      url = 'https://github.com/cheneydc/qnupload',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          'console_points':[
              'qnupload = qnupload.qnupload:main'
          ]
      },
)
