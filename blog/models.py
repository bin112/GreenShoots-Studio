# -*-coding:utf-8 -*-
#
# Created on 2015-01-06, by Felix
#
#
__author__ = 'chengbin.wang'

from django.db import models
from core.models import Basemodel
from user.models import User
from django.db.models.signals import m2m_changed, pre_save, pre_delete
from django.core.urlresolvers import reverse


class Base(Basemodel):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    count = models.IntegerField(default=0, verbose_name=u'引用次数')
    slug = models.SlugField(max_length=200, unique=True, verbose_name=u'链接名')

    def __unicode__(self):
        return self.name

    def incr(self, num=1):
        self.count += num
        self.save()

    def decr(self, num=1):
        self.count += num
        self.save()

    class Meta:
        abstract = True


class Tag(Base):

    class Meta:
        db_table = 'blog_tag'
        verbose_name = u'标签'
        verbose_name_plural = u'标签'


class Category(Base):

    class Meta:
        db_table = 'blog_theme'
        verbose_name = u'分类'
        verbose_name_plural = u'分类'


class BlogQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)


class Blog(Basemodel):
    title = models.CharField(max_length=25, verbose_name=u'标题')
    category = models.ForeignKey(Category, verbose_name=u'主题', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name=u'标签', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, verbose_name=u'链接名')
    content = models.TextField(verbose_name=u'正文')
    image = models.ImageField(upload_to='blog', verbose_name=u'题图', blank=True, null=True)
    author = models.ForeignKey(User, verbose_name=u'作者')
    is_published = models.BooleanField(default=True, verbose_name=u'是否发布')
    click_count = models.IntegerField(default=0, editable=False, verbose_name=u'点击量')
    comment_count = models.IntegerField(default=0, editable=False, verbose_name=u'评论数')
    objects = BlogQuerySet.as_manager()

    def click(self):
        self.click_count += 1
        self.save()

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-create_time"]
        verbose_name = u'博客'
        verbose_name_plural = u'博客'


def handle_in_batches(instances, method):
    for item in instances:
        getattr(item, method)()


def blog_pre_save(sender, **kwargs):
    try:
        blog = Blog.objects.get(id=kwargs.get('instance').id)
    except Blog.DoesNotExist:
        kwargs.get('instance').category.incr()
    else:
        pass


def blog_pre_delete(sender, **kwargs):
    ins = kwargs.get('instance')
    ins.category.decr()
    handle_in_batches(ins.tags.all(), 'decr')


def tags_pre_save(sender, **kwargs):
    if kwargs.get('action') == 'pre_clear':
        handle_in_batches(kwargs.get('instance').tags.all(), 'decr')
    elif kwargs.get('action') == 'post_remove':
        handle_in_batches(Tag.objects.filter(id__in=kwargs.get('pk_set')), 'decr')
    elif kwargs.get('action') == 'post_add':
        handle_in_batches(Tag.objects.filter(id__in=kwargs.get('pk_set')), 'incr')


pre_save.connect(blog_pre_save, sender=Blog)
pre_delete.connect(blog_pre_delete, sender=Blog)
m2m_changed.connect(tags_pre_save, sender=Blog.tags.through)