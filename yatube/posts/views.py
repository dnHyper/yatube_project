from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком постов
def group_posts(request, slug):
    return HttpResponse('Список постов, отфильтрованный по группам')


def group(request):
    return HttpResponse('Список групп')
