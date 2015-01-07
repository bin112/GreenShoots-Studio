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


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "create_time")
    readonly_fields=('click_count',)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "count")

class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "count")

class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "count")

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
