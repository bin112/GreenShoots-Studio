# -*-coding:utf-8 -*-
#
# Created on 2015-01-06, by Felix
#
#
__author__ = 'chengbin.wang'

from django.views import generic
from . import models


class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class BlogIndex(ExtraContext, generic.ListView):
    extra_context = {"categories": models.Category.objects.all()}
    template_name = "blogs.html"
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs.get('slug', None)
        if slug:
            return models.Blog.objects.published().filter(category__slug=slug)
        else:
            return models.Blog.objects.published()


class BlogDetail(ExtraContext, generic.DetailView):
    extra_context = {"categories": models.Category.objects.all()}
    model = models.Blog
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        self.object.click_count += 1
        self.object.save()
        return context