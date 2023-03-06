from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import News, Category


def home(request):
    return HttpResponse("Сайт з новинами :)")


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'news/all_category.html', {'categories': categories})


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    news = News.objects.filter(categories=category)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'news/news_detail.html', {'news': news})


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не існує</h1>")
