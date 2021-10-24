#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：app_base_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 14:50
from page_objects.base_page import BasePage


class AppBasePage(BasePage):
    name = 'app base 页面'

    def get_device_size(self):
        """
        获取设备屏幕大小
        :return:
        """
        size = self.driver.get_window_size()
        return size['width'], size['height']