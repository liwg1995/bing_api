#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/27 下午6:01
# @Author  : Wugang Li
# @File    : Hello.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return 'Hello Flask!'