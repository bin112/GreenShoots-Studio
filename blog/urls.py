from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.BlogList.as_view(), name="blog"),
    url(r'^category/(?P<slug>\S+)/$', views.BlogList.as_view(), name="category_blogs"),
    url(r'^tag/(?P<pk>\S+)/$', views.BlogList.as_view(), name="tag_blogs"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="blog_detail"),
)
