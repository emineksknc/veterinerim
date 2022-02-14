# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


# Create your views here.
def home_view(request):
    if request.user.is_authenticated():
        context = {
            'isim': 'Emine'
        }
    else:
        context = {
            'isim': 'Guest'
        }
    return render(request, 'home.html', context)
