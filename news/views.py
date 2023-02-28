from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def home(request):
    return HttpResponse("Новини")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не існує</h1>")
