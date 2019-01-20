from django.conf.urls import url
from booktest import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^(\d+)/$', views.detail),
    url(r'^create/$', views.create),
    url(r'^delete/(\d+)/$', views.delete),
]
