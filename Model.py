#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/25 下午5:22
# @Author  : olei
# @File    : Model.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Bing(db.Model):
    __tablename__ = "psql_bing"
    id = db.Column(db.Integer,unique=True,primary_key=True)
    dates = db.Column(db.Date,nullable=False)
    bing_url = db.Column(db.String(10000),nullable=False)
    qiniu_url = db.Column(db.String(10000),nullable=False)
    image_name = db.Column(db.String(10000),nullable=False)
