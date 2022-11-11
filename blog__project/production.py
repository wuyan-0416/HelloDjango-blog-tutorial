# -*- codeing = utf-8 -*-
# @Time  :2022/11/10 16:22
# @Author:wuyan
# @File  :production.py
# @Software :PyCharm

from .common import *
# 用于存放线上环境的配置
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['hellodjango-blog-tutorial-demo.zmrenwu.com']

