#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

VERSION = '1.2'

setup(name = 'qnupload',
      version = VERSION,
      description = 'Tool to upload file to Qiniu cloud',
      keywords = 'python qnupload terminal',
      author = 'cheneydc',
      author_email = 'cheneydc@gmail.com',
      url = 'https://github.com/cheneydc/qnupload',
      license='MIT',
      package_dir = {'':'src'},
      packages=find_packages('src'),
      include_package_data=True,
      entry_points={
          'console_scripts':[
              'qnupload = qnupload.qnupload:main',
          ]
      },
      install_requires=[
          'qiniu',
      ],
      data_files=[
          ('/etc/qnupload', ['etc/qnupload/qnupload.conf']),    
      ],
)
