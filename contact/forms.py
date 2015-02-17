# -*-coding:utf-8 -*-
#
# Created on 2015-02-01
#
#

from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(max_length=10, label=u'名称', required=False)
    phone = forms.CharField(max_length=18, label=u'电话号码', required=False)
    email = forms.EmailField(max_length=150, label=u'邮箱地址', required=False)
    description = forms.CharField(label=u'留言内容', widget=forms.Textarea, required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError(u'请输入名称！！')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError(u'请输入号码！！')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError(u'请输入邮箱啊')
        return email

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError(u'请输入描述呢')
        return description


    # class Meta:
    #     model = Contact
    #     fields = ('name', 'phone', 'email', 'description')

