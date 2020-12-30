# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/28 17:15 
# @Author : River 
# @File : test_fabric_base.py
# @desc :
"""
import time

from plm_web.fabric_base_page import FabricBasePage

page = FabricBasePage()


def test_add_fabric_info():
    page.plm_login()
    page.get()
    page.add_fabric_info()
    time.sleep(10)
