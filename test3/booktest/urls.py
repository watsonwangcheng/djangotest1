# -*- coding:utf-8 -*-
#!/usr/bin/python
#######################################
#     > Mail: 1134314189@qq.com 
#     > Created Time: 2020年10月31日 星期六 03时11分46秒
#     > Author: watson
#     > File Name: urls.py
######################################################
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
]
