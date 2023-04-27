from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import News, Category


menu = [{'title': 'Про сайт', 'url_name': 'news:about'},
        {"title": "Добавити статтю", 'url_name': 'news:add_article'},
        {'title': "Увійти", "url_name": 'news:login'}]


def index(request):
    category = Category.objects.all()
    context = {'title': 'Головна сторінка',
               'menu': menu,
               'category': category}
    return render(request, 'news/index.html', context=context)


def about(request):
    category = Category.objects.all()
    context = {'title': 'Про сайт',
               'menu': menu,
               'category': category}
    return render(request, 'news/index.html', context=context)


def add_article(request):
    category = Category.objects.all()
    context = {'title': 'Додати статтю',
               'menu': menu,
               'category': category}
    return render(request, 'news/index.html', context=context)


def login(request):
    category = Category.objects.all()
    context = {'title': 'Увійти в акаунт',
               'menu': menu,
               'category': category}
    return render(request, 'news/index.html', context=context)


def category(request, parameter):
    category = Category.objects.get(name=parameter)
    category_article = News.objects.filter(categories=category.pk)
    category = Category.objects.all()
    context = {'title': parameter,
               'menu': menu,
               'category': category,
               'article': category_article}
    print(category_article)
    return render(request, 'news/category.html', context=context)


def article(request, article_id):
    return HttpResponse(f"Допис - {article_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не існує</h1>")
