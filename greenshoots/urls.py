from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^work/$', TemplateView.as_view(template_name='work.html'), name='work'),
    url(r'^blog/$', TemplateView.as_view(template_name='blog.html'), name='blog'),
    url(r'^team/$', TemplateView.as_view(template_name='team.html'), name='team'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
)
