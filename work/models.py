# -*-coding:utf-8 -*-
#
# Created on 2015-01-09
#
#

from core.models import Basemodel
from django.db import models


class ProductImage(Basemodel):
    name = models.CharField(max_length=20, verbose_name=u'图片名称')
    image = models.ImageField(upload_to="product", verbose_name=u'产品图片')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'产品图片'
        verbose_name_plural = u'产品图片'


class Product(Basemodel):
    name = models.CharField(max_length=25, verbose_name=u'产品名称')
    picture = models.ForeignKey(ProductImage, verbose_name=u'产品图片', blank=True, null=True)
    product_url = models.URLField(verbose_name=u'产品链接', blank=True, null=True)
    description = models.TextField(verbose_name=u'产品描述', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = u'产品'