# -*-coding:utf-8 -*-
#
# Created on 2015-02-01
#
#

from django.template import RequestContext
from django.views.generic import View
from django.shortcuts import render_to_response
from contact.models import Contact
from .forms import ContactForm


class ContactUs(View):
    """
    联系我们
    """

    def post(self, request):
        message = ''
        error = ''
        mydict = {}
        form = ContactForm(request.POST)
        if form.is_valid():
            print form.cleaned_data, '###########', form
            ctx = {
                'name': form.cleaned_data.get('name'),
                'phone': form.cleaned_data.get('phone'),
                'email': form.cleaned_data.get('email', ''),
                'description': form.cleaned_data.get('description')
            }
            Contact.objects.create(**ctx)
            message = u'提交成功'
        for i, j in form.errors.items():
            print i, j
            mydict[i] = j
        print mydict, '####'
        if mydict.has_key('name'):
            error = mydict['name']
        elif mydict.has_key('phone'):
            error = mydict['phone']
        elif mydict.has_key('email'):
            error = mydict['email']
        elif mydict.has_key('description'):
            error = mydict['description']

        return render_to_response('contact.html', {'form': form, 'error': error}, context_instance=RequestContext(request))


    def get(self, request):
        form = ContactForm()

        return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))