from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from firstapp.models import men, Category


# Create your views here.


def title(request):
    ps = men.objects.all()
    context = {
        'title': 'Главная страница',
        'top': ps,
        'cat_selected': 0
    }
    return render(request, 'firstapp/index.html', context=context)


def about(request):
    return render(request, 'firstapp/about.html', {'title': 'О сайте'})


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

def show_category(request, cat_id):
    ps = men.objects.filter(cat_id=cat_id)
    if len(ps) == 0:
        raise Http404
    context = {
        'title': 'Отображение по рубрикам',
        'top': ps,
        'cat_selected': cat_id
    }
    return render(request, 'firstapp/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Вы ввели неизвестный для маршрутизатора запрос</p>')