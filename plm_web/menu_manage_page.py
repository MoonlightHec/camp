# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/26 17:08 
# @Author : River 
# @File : menu_manage_page.py
# @desc : 菜单管理页面
"""
import time

from plm_web.base_page import BasePages


class MenuManagePage(BasePages):

    def get(self):
        self.driver.get("http://plm.hqygou.com:8087/#/system_setting/rbac/menu/list")

    def add_menu(self, menu_name):
        """
        菜单管理-添加菜单
        :return:
        """
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/button').click()
        self.driver.find_element_by_xpath('//label[@for="menuName"]/following-sibling::div/div/input').send_keys(
            menu_name)
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="el-dialog__footer"]/div/button[2]').click()

    def update_menu(self, menu_name):
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[4]/div[3]/table/tbody/tr[4]/td[7]/div/button[2]').click()
        self.driver.find_element_by_xpath('//label[@for="menuName"]/following-sibling::div/div/input').clear()
        self.driver.find_element_by_xpath('//label[@for="menuName"]/following-sibling::div/div/input').send_keys(
            menu_name)
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="el-dialog__footer"]/div/button[2]').click()
