from django.conf.urls import url

from students import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^myprofile/', views.MyProfileView.as_view(), name='myprofile')
]
