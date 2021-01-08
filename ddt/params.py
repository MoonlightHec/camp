# _*_ coding: utf-8 _*_
"""
# @Time : 2021/1/8 16:03 
# @Author : River 
# @File : params.py
# @desc :
"""
import yaml

datas = None
# 读取数据驱动的参数
with open('../ddt/login_page.yaml', encoding='utf-8') as f2:
    datas = yaml.safe_load(f2)
