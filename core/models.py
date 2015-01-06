# -*-coding:utf-8 -*-
#
# Created on 2015-01-06, by Felix
#
#
__author__ = 'chengbin.wang'

from django.db import models


class Basemodel(models.Model):
    is_active = models.BooleanField(verbose_name=u'是否有效', default=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-create_time']