from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^process/$', views.process, name='process'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^deleted/(?P<id>\d+)/$', views.deleted, name='deleted'),
]
