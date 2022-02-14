from django.conf.urls import url
from django.contrib import admin

app_name = 'petowner'

from .views import *

urlpatterns = [

    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^profile/$', profile, name='profile'),


]
