from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from firstapp.models import men

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

# Create your views here.


def title(request):
    ps = men.objects.all()
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'top': ps
    }
    return render(request, 'firstapp/index.html', context=context)


def about(request):
    return render(request, 'firstapp/about.html', {'title': 'О сайте', 'menu': menu})


def goroot(request):
    return redirect('root')


def addpage(request):
    return HttpResponse('Добавьте статью')


def contact(request):
    return HttpResponse('Оставьте сообщение')


def login(request):
    return HttpResponse('Ведите логин и пароль')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи {post_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Вы ввели неизвестный для маршрутизатора запрос</p>')