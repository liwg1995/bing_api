#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/27 下午6:13
# @Author  : Wugang Li
# @File    : Date.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_restful import Resource,abort,marshal
from Common.Public import Common,resource_full_fields
from Model import Bing

class Bing_url(Resource):
    def get(self, dates):
        dates = Bing.query.filter_by(dates=dates).first()
        if (dates is None):
            abort(410, msg="找不到数据！", data=None, status=0)
        else:
            return Common.returnTrueJson(Common, marshal(dates, resource_full_fields))
