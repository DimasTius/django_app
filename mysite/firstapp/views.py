from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
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


def show_post(request, post_slug):
    post = get_object_or_404(men, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, 'firstapp/post.html', context=context)


def show_category(request, cat_slug):
    ps = men.objects.filter(cat__slug=cat_slug)
    if len(ps) == 0:
        raise Http404
    context = {
        'title': 'Отображение по рубрикам',
        'top': ps,
        'cat_selected': cat_slug
    }
    return render(request, 'firstapp/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Вы ввели неизвестный для маршрутизатора запрос</p>')