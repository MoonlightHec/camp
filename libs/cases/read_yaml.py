# _*_ coding: utf-8 _*_
"""
# @Time : 2021/1/8 11:43 
# @Author : River 
# @File : read_yaml.py
# @desc : 读取yaml文件内容为字典
"""
import pytest_util.sort_yaml as oy

from mysuites.webkeys import WebKey

# 读取yaml文件
datas = oy.ordered_yaml_load('./cases.yaml')
web_key = WebKey()

# 将数据写为yaml文件
with open('./t1.yaml', 'w', encoding='utf8') as stream:
    print(datas)
    oy.ordered_yaml_dump(datas, stream, allow_unicode=True)

list_cases = datas['loginPage']
login_case = list_cases[0]['cases']
for cases in login_case:
    list_case = list(cases.values())
    values = list_case[1:-1]
    print(list_case)
    print(values)
    # function = getattr(web_key, list_case[0])
    # values = list_case[0:]
