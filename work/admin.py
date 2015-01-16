# -*-coding:utf-8 -*-
#
# Created on 2015-01-09
#
#

from django.contrib import admin
from .models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)