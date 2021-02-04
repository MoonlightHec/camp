# _*_ coding: utf-8 _*_
"""
# @Time : 2021/1/27 11:14 
# @Author : River 
# @File : db_es.py
# @desc : 读取数据库
"""

import pymysql

connect = pymysql.connect(
    host='10.40.6.150',
    port=3306,
    user='java-service',
    passwd='java123456',
    db='pay',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()
