#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：login_page_locators.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 16:13
from appium.webdriver.common.mobileby import MobileBy as By


class LoginPageLocators:
    # ========================未登录==============================
    # 用户名输入框
    username_input_loc = (By.ID, 'com.lemon.lemonban:id/et_mobile')
    # 密码输入框
    password_input_loc = (By.ID, 'com.lemon.lemonban:id/et_password')
    # 登录按钮
    login_btn_loc = ('xpath', '//*[@text="登录"]')
    # 获取错误操作信息
    error_info_loc = ('xpath', '//*[@class="android.widget.Toast"]')
    # 关闭图标
    close_img_loc = ('xpath', '//*[@class="android.widget.ImageButton"]')
    # =======================已登录======================================
    # 设置按钮
    settings_btn_loc = ('xpath', '//*[@class="android.widget.ImageButton"]')
