from django.conf.urls import url
from rango import views
from django.conf import settings


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^$', views.about, name='about'),
        ]
