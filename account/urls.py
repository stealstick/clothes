from django.conf.urls import include, url
from . import views

urlpatterns = [
     url(
        r'^login/',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={
            'template_name': 'account/login.html'
        }
    ),
    url(
        r'^logout/',
        'django.contrib.auth.views.logout',
        name='logout',
    ),
    url(r'^signup/$', views.signup),
    url(r'^useradd$', views.useradd),   
]

