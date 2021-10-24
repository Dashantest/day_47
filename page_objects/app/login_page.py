#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：login_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 16:11
from page_objects.app.app_base_page import AppBasePage
from page_locators.app.login_page_locators import LoginPageLocators


class LoginPage(AppBasePage):
    """
    把每个页面抽象成一个类，所有这个页面上的功能封装成方法
    """
    name = '登录页面'

    def login(self, mobile, password):
        """
        登录页面的登录功能
        :param mobile:
        :param password:
        :return:
        """
        # 1.启动app进入首页
        # with webdriver.Remote(self.settings.APPIUM_SERVER_HOST,
        #                       desired_capabilities=self.settings.DESIRED_CAPS) as session:
        #     # 点击我的柠檬
        #     np = NavigationPage(session)
        #     np.switch_navigation('我的柠檬')
            # 点击头像登录
        # self.wait_element_is_visible(MyPageLocators.header_img, '点击我的头像').click_element()
        # # 延时操作
        # self.delay()
        # 2.输入用户名、密码
        # 2.1定位用户名输入框
        # 2.2输入用户名
        self.wait_element_is_visible(LoginPageLocators.username_input_loc, '登录').send_keys(mobile)
        # 2.3定位密码输入框
        # 2.4输入密码
        self.wait_element_is_visible(LoginPageLocators.password_input_loc, '登录').send_keys(password)
        # 3.点击登录
        self.wait_element_is_visible(LoginPageLocators.login_btn_loc, '登录').click_element()

    def get_error_tip(self):
        """
        获取登录错误信息
        :return:
        """
        # find_element需要by用*解包可以得到
        # return self.driver.find_element(*LoginPageLocators.error_info_tip_loc).text
        error_tip = self.wait_element_is_loaded(LoginPageLocators.error_info_loc, '获取错误信息').get_element_text()
        return error_tip

    def close_login_page(self):
        """
        关闭登录页面
        :return:
        """
        self.wait_element_is_visible(LoginPageLocators.close_img_loc, '关闭登录页面').click_element()
