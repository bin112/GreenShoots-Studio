from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.BlogIndex.as_view(), name="blog"),
    url(r'^category/(?P<slug>\S+)/$', views.BlogIndex.as_view(), name="category_blogs"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="blog_detail"),
)
