from django.urls import path

from .views import *
app_name = 'news'

urlpatterns = [
    path('', index, name='home'),
    path("about/", about, name='about'),
    path("add_article/", add_article, name='add_article'),
    path("login/", login, name='login'),
    path("category/<str:parameter>", category, name='category'),
    path("article/<int:article_id>", article, name='article'),
]
