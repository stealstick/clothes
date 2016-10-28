from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^send/(?P<username>.+)$', views.send),
    url(r'^category/(?P<category>.+)$', views.category),
]
