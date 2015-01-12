# -*-coding:utf-8 -*-
#
# Created on 2015-01-09
#
#

from django.shortcuts import render, render_to_response
from django.views.generic import View, ListView
from core.views import ExtraContextMixin
from work.models import Product

# Create your views here.


class ProductList(ListView):
    template_name = 'work.html'
    model = Product



