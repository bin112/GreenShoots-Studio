# -*-coding:utf-8 -*-
#
# Created on 2015-02-01
#
#

from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    exclude = ('is_active',)


admin.site.register(Contact, ContactAdmin)



