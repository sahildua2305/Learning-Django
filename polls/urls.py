#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2015-12-25 03:17:44
# @Last Modified by:   sahildua2305
# @Last Modified time: 2015-12-25 03:31:27

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
