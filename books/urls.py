#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from books import views
from books.views import SpecificIndexView

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^select/$', views.SelectorView.as_view(), name='select'),
    url(r'^(?P<languages>[\w\-\*]+)/(?P<techs>[\w\-\*]+)/(?P<tags>[\w\-\*]+)/$', SpecificIndexView.as_view(), name='specific_index'),
    url(r'^rest/status/update/$', views.StatusUpdateView.as_view(), name='status_update')
]
