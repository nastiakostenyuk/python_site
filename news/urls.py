from django.urls import path

from .views import *
app_name = 'news'

urlpatterns = [
    path("", index, name='home'),
    path("about", about, name='about')
]
