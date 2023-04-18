from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import News, Category


menu = ['Про сайт', "Добавити статтю", "Увійти"]


def index(request):
    return render(request, 'news/index.html', {'title': 'Головна сторінка', 'menu': menu})


def about(request):
    return render(request, 'news/index.html', {'title': 'Про сайт', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не існує</h1>")
