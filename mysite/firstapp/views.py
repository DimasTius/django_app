from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from firstapp.models import men

menu = ('О сайте', 'Добавить статью', 'Обратная связь', 'Войти')
# Create your views here.


def title(request):
    ps = men.objects.filter(pk__lte=3)
    return render(request, 'firstapp/index.html', {'title': 'Главная страница', 'menu': menu, 'top': ps})


def about(request):
    return render(request, 'firstapp/about.html', {'title': 'О сайте', 'menu': menu})

def goroot(request):
    return redirect('root')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Вы ввели неизвестный для маршрутизатора запрос</p>')