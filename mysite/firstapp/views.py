from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
def title(request):
    return HttpResponse('<h1>welcome</h1>')

def sports(request, sportid): #HttpRequest
    if request.GET:
        print(request.GET)
    return HttpResponse(f'page sport: {sportid}')

def archive(request, year):
    if int(year) > 2023:
        raise Http404
    return HttpResponse(f'<h1>Архив за {year} год</h1>')

def goroot(request):
    return redirect('root')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Вы ввели неизвестный для маршрутизатора запрос</p>')