#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：my_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/26 15:41
from page_objects.app.app_base_page import AppBasePage
from page_locators.app.my_page_locators import MyPageLocators


class MyPage(AppBasePage):
    name = '我的柠檬页面'

    def click_header(self):
        """
        点击我的头像
        :return:
        """
        self.wait_element_is_visible(MyPageLocators.header_img, '点击我的头像').click_element()

    def my_lemon_avatar_title(self):
        """
        获取登录成功后的昵称
        :return:
        """
        return self.wait_element_is_visible(MyPageLocators.my_lemon_title_loc, '获取登录成功后昵称').get_element_text()

    def get_login_out_toast(self):
        """
        获取登出成功后的toast
        :return:
        """
        return self.wait_element_is_loaded(MyPageLocators.login_out_toast_loc, '获取登出提示信息').get_element_text()