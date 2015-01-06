# -*-coding:utf-8 -*-
#
# Created on 2015-01-06, by Felix
#
#
__author__ = 'chengbin.wang'

from django.db import models
from core.models import Basemodel


class User(Basemodel):
    name = models.CharField(max_length=25, verbose_name=u'姓名', unique=True, db_index=True)
    password = models.CharField(max_length=128, verbose_name=u'密码', default='')
    status = models.CharField(max_length=1, verbose_name=u'用户状态', choices= (
        ('S', u'启用'),
        ('F', u'禁用'),
    ))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


class Basicinfo(Basemodel):
    user = models.OneToOneField(User, verbose_name=u'用户')
    nickname = models.CharField(max_length=30, verbose_name=u'昵称')
    avatar = models.ImageField(upload_to='user/basicinfo', verbose_name=u'头像')
    sex = models.CharField(max_length=1, verbose_name=u'性别', choices= (
        ('M', u'男'),
        ('F', u'女')
    ), blank=True)
    email = models.EmailField(verbose_name=u'邮箱', blank=True)
    qq = models.CharField(max_length=15, verbose_name=u'qq账号', blank=True)
    signature = models.CharField(max_length=300, verbose_name=u'个性签名', blank=True)

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name = u'用户资料'
        verbose_name_plural = u'用户资料'