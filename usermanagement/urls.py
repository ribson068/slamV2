# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from usermanagement.views import signup




urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^Signup/$', signup, name='signup'),
    
]
