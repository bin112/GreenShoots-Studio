# -*-coding:utf-8 -*-
#
# Created on 2015-01-06, by Felix
#
#
__author__ = 'chengbin.wang'

from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "basicinfo", "update_time", "create_time")

class BasicinfoAdmin(admin.ModelAdmin):
    list_display = ("user", "sex")

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Basicinfo, BasicinfoAdmin)