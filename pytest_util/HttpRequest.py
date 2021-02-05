# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/4 14:55 
# @Author : River 
# @File : HttpRequest.py
# @desc :
"""
import json

import requests


class HttpRequest:

    @staticmethod
    def get(url, headers=None, params=None):
        """
        :param url: 请求地址
        :param headers: 请求头
        :param params: 请求参数
        :return:
        """
        response = requests.get(url, headers=headers, params=params).json()
        output = json.dumps(response, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
        return output

    @staticmethod
    def post(url, headers=None, body=None):
        """
        :param url: 请求地址
        :param headers: 请求头
        :param body: 请求body
        :return:
        """
        headers_type = headers.get("Content-Type")
        if headers_type == "application/json":
            response = requests.post(url, headers=headers, json=body).json()
        elif headers_type == "application/x-www-form-urlencoded":
            response = requests.post(url, headers=headers, data=body).json()
        else:
            print("请求参数格式不支持")
        output = json.dumps(response, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
        return output
