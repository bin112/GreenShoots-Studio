from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value):
    return value[:200]