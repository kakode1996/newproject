from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    url('edit/(?P<id>\d+)', views.edit),
    url('update/(?P<id>\d+)', views.update), #do not put / like this url('delete/(?P<id>\d+)/ ok. put ->url('delete/(?P<id>\d+)
    url('delete/(?P<id>\d+)/', views.destroy),
]