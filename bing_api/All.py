#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/27 下午6:09
# @Author  : Wugang Li
# @File    : All.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_restful import Resource,marshal
from Common.Public import Common,resource_full_fields
from Model import Bing

class Bing_all(Resource):
    def get(self):
        # dates = Bing.query.filter_by()
        return Common.returnTrueJson(Common, marshal(Bing.query.all(), resource_full_fields))

