from django.conf.urls import url
from django.contrib import admin

app_name = 'pet'

from .views import *
urlpatterns = [
    url(r'^index/$', pet_index, name='index'),
    url(r'^(?P<id>\d+)/$', pet_detail, name='detail'),  #create dynamic url with id parameter
    url(r'^create/$', pet_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', pet_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', pet_delete, name='delete'),

]
