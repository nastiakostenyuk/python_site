from django.urls import path

from .views import *
app_name = 'news'

urlpatterns = [
    path("news/", home, name='home'),
    path('category/all', all_categories, name='all_categories'),
    path('category/<int:category_id>', category, name='category'),
    path('news/<int:news_id>', news_detail, name='news_detail'),
]
