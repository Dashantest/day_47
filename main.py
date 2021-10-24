#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：main.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/6 8:56

import pytest

import settings

if __name__ == '__main__':
    pytest.main([
        '-s',
        '-v',
        # '-m',
        # 'success',
        # settings.TEST_CASE_DIR
        r'C:\Users\zhengshan\Desktop\day_47\testcases\app'
    ])
# jjffjfj