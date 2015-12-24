#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2015-12-25 03:17:44
# @Last Modified by:   sahildua2305
# @Last Modified time: 2015-12-25 03:31:31

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, at index!")
