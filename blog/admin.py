# -*-coding:utf-8 -*-
#
# Created on 2015-01-06, by Felix
#
#
__author__ = 'chengbin.wang'

from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "count")
    readonly_fields = ('slug',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "create_time", "slug",)
    #exclude = ('slug',)
    readonly_fields = ('click_count', 'slug')


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "count")
    readonly_fields = ('slug',)

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
