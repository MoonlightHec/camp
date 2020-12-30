# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/28 17:02 
# @Author : River 
# @File : fabric_base_page.py
# @desc : 面料基础档案页面
"""
import time

from plm_web.base_page import BasePages


class FabricBasePage(BasePages):
    def get(self):
        self.driver.get("http://plm.hqygou.com:8087/#/fabric_manage/basic_archives/basic_archives/list")

    def add_fabric_info(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/button[1]/span').click()

        self.driver.find_element_by_xpath('//div[@class="basic-info-box"]/div[3]/div[1]/div/div/div/div/input').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
