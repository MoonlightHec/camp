# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/19 16:39 
# @Author : River 
# @File : db.py
# @desc :
"""
import os

import pymysql

from pytest_util import sort_yaml


def get_cursor(database):
    # 获取当前文件db.py绝对路径
    path = os.path.dirname(os.path.abspath(__file__))
    datas = sort_yaml.ordered_yaml_load(path + '/db_config.yaml')

    db_config = datas[database]
    host = db_config['host']
    port = db_config['port']
    user = db_config['user']
    passwd = db_config['passwd']
    db = db_config['db']
    charset = db_config['charset']

    connect = pymysql.connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=db,
        charset=charset
    )
    # 获取游标
    return connect.cursor()
