# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/26 16:19 
# @Author : River 
# @File : test_menu_manage.py
# @desc :
"""
import time

from plm_web.menu_manage_page import MenuManagePage

page = MenuManagePage()


def test_add_menu():
    """
    依赖登录
    添加菜单
    :return:
    """
    page.plm_login()
    time.sleep(3)
    page.get()
    page.update_menu("菜单测试update")
    time.sleep(3)


def test_update_menu():
    page.update_menu("菜单测试update2")
    page.quit()



