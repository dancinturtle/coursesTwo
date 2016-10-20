from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^courses/destroy/(?P<id>\d+)$', views.confirmDelete),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^courses/comment/(?P<id>\d+)$', views.viewComments),
    url(r'^addComment$', views.addComment)
]
