""" Hello World app for deploying Python functions as APIs on Bluemix """ 
# Always prefer setuptools over distutils 
from setuptools import setup, find_packages 
from codecs import open 
from os import path 
here = path.abspath(path.dirname(__file__)) 
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read() 
setup( 
name='api_server', 
version='1.0.0', 
description='Running Python apps on Bluemix', long_description=long_description, 
url='https://github.com/elseagle/sentiment_analysis', license='Apache-2.0' 
)
