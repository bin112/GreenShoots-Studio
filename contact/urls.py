# -*-coding:utf-8 -*-
#
# Copyright (C) 2012-2014 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-01-12, by chengbin.wang
#
#
__author__ = 'chengbin.wang'

from django.conf.urls import patterns, url
from .views import ContactUs

urlpatterns = patterns('',
                       url(r'^$', ContactUs.as_view(), name="contact"),
)

