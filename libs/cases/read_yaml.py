# _*_ coding: utf-8 _*_
"""
# @Time : 2021/1/8 11:43 
# @Author : River 
# @File : read_yaml.py
# @desc : 读取yaml文件内容为字典
"""
import yaml
from mysuites.webkeys import WebKey

with open('./cases.yaml', encoding='utf-8') as f2:
    datas = yaml.safe_load(f2)

web_key = WebKey()

list_cases = datas['loginPage']

login_case = list_cases[0]['cases']
for cases in login_case:
    list_case = list(cases.values())
    function = getattr(web_key, list_case[1])
    values = list_case[0:]
