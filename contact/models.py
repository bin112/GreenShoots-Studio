# -*-coding:utf-8 -*-
#
# Created on 2015-02-01
#
#


from django.db import models
from core.models import Basemodel


class Contact(Basemodel):
    name = models.CharField(max_length=10, verbose_name=u'姓名', blank=True, null=True)
    phone = models.CharField(max_length=18, verbose_name=u'联系电话', blank=True, null=True)
    email = models.EmailField(verbose_name=u'邮箱', blank=True, null=True)
    description = models.TextField(verbose_name=u'需求描述', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'联系我们'
        verbose_name_plural = u'联系我们'
