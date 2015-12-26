#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2015-12-25 03:17:44
# @Last Modified by:   sahildua2305
# @Last Modified time: 2015-12-26 20:25:56

from django.contrib import admin

from .models import Question

admin.site.register(Question)
