# -*- codeing = utf-8 -*-
# @Time  :2022/11/3 17:42
# @Author:wuyan
# @File  :urls.py
# @Software :PyCharm

from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]