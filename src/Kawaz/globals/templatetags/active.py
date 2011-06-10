# -*- coding: utf-8 -*-
#
# Created:    2010/10/13
# Author:         alisue
#
from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    from re import search
    if search(pattern, request.path):
        return 'active'
    return ''