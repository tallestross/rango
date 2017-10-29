from django.conf.urls import url
from rango import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
        url(r'^$', views.index, name='index'),
        ]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
