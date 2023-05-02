from django.urls import path, re_path

from . import views

urlpatterns = [
    # ex: /intro/
    re_path('^.*', views.index, name='index'),
    # add your routing here
]