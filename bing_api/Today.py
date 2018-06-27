#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/27 下午6:14
# @Author  : Wugang Li
# @File    : Today.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_restful import Resource,abort,marshal
from Common.Public import Common,resource_full_fields
from Model import Bing
import datetime

class New_url(Resource):
    def get(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        dates = Bing.query.filter_by(dates=today).first()
        if (dates is None):
            abort(410,msg="今天的图片没有采集到",data=None,status=0)
        else:
            return Common.returnTrueJson(Common,marshal(dates,resource_full_fields))