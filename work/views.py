# -*-coding:utf-8 -*-
#
# Created on 2015-01-09
#
#

from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from django.views.generic import View, ListView, DetailView
from core.views import ExtraContextMixin
from work.models import Product

# Create your views here.


class ProductList(ExtraContextMixin, ListView):
    template_name = 'work.html'
    model = Product
    paginate_by = 12
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'workdetail.html'
    context_object_name = 'work_detail'
