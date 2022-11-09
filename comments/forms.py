# -*- codeing = utf-8 -*-
# @Time  :2022/11/3 11:25
# @Author:wuyan
# @File  :forms.py
# @Software :PyCharm


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
