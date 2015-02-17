# -*-coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import settings

admin.site.site_header = '绿芽管理后台'
admin.site.site_title = "工作室"
admin.site.index_title = "绿芽"

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^work/', include('work.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^team/$', TemplateView.as_view(template_name='team.html'), name='team'),
    url(r'^contact/$', include('contact.urls'), name='contact'),
    url(r'^services/$', TemplateView.as_view(template_name='services.html'), name='services'),
    url(r'^ueditor/', include('DjangoUeditor.urls' )),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    )