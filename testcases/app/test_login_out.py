#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：test_login_out.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/26 16:22
from testcases.base_test_case import BaseCase
from page_objects.app.navigation_page import NavigationPage
from page_objects.app.settings_page import SettingsPage


class TestLoginOut(BaseCase):
    name = '登出功能'

    def test_login_out(self, login_driver):
        self.logger.info('**********{}开始测试**********'.format(self.name))
        # 前置为已登录，通过夹具实现
        # 点击我的柠檬，保证后面可以定位到设置
        self.driver = login_driver
        np = NavigationPage(login_driver)
        np.click_my()
        # 点击设置
        sp = SettingsPage(login_driver)
        sp.click_settings()
        # 点击退出
        sp.click_login_out_btn()
        # 点击弹框的确认
        sp.click_confirm()
        # 断言
        self.assert_equal(sp.get_logout_toast(), '退出登录成功')
        self.logger.info('**********{}测试结束**********'.format(self.name))