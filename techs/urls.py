from django.conf.urls import url

from techs import views
from techs.views import CategoryIndexView

urlpatterns = [
    url(r'^main/$', views.MainView.as_view(), name='main'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<category>[\w]+)/$', CategoryIndexView.as_view(), name='category-index'),
]
