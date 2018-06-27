#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/26 上午11:21
# @Author  : olei
# @File    : app.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask import Flask, jsonify
from Model import db
from flask_restful import Api
from Common.Public import errors
from bing_api import Hello,Date,Today,All

app = Flask(__name__)
app.config.from_object("Config")

db.init_app(app)

api = Api(app,catch_all_404s=True,errors=errors)


api.add_resource(Hello.Hello, '/', '/hello')
api.add_resource(All.Bing_all, '/bing')
api.add_resource(Date.Bing_url, '/bing/<string:dates>')
api.add_resource(Today.New_url,'/bing/today')

