#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/25 下午5:15
# @Author  : olei
# @File    : Config.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

DB_USER = "postgres"
DB_PASSWORD = "postgres"
HOST = "127.0.0.1"
DB_NAME = "bing"


DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USER + ':' + DB_PASSWORD + "@" + HOST + '/' + DB_NAME
