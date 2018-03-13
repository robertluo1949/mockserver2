#coding:utf-8
'''
title:mock server   control
author:Robert
date:20180123
email:luoshuibo@vcredut.com
content:
other:
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'