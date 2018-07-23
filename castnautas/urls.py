from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('<int:page_num>', index, name='index'),
    path('post/<str:titulo>',post,name='post'),
    path('busca/<str:tag>/<int:page_num>/',busca,name='busca'),


]
