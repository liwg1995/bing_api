#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/27 下午6:03
# @Author  : Wugang Li
# @File    : Public.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask import Flask,jsonify
from Model import db
from flask_restful import Api,fields,reqparse



errors = {
    'BingAlreadyExistsError': {
        'message': "It is already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

parser = reqparse.RequestParser()
parser.add_argument('dates', required=True)
parser.add_argument('bing_url', required=True)
parser.add_argument('qiniu_url', required=True)
# parser.add_argument('user_nickname')
parser.add_argument('image_name', required=True)

resource_full_fields = {
    'id': fields.Integer,
    'dates': fields.String,
    'bing_url': fields.String,
    'qiniu_url': fields.String,
    'image_name': fields.String
}

class Common:
    def returnTrueJson(self, data, msg="请求成功"):
        return jsonify({
            "status": 1,
            "data": data,
            "msg": msg
        })

    def returnFalseJson(self, data=None, msg="请求失败"):
        return jsonify({
            "status": 0,
            "data": data,
            "msg": msg
        })