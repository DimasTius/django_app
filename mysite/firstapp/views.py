from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from firstapp.models import men, Category
from .forms import AddPostForm

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]
# Create your views here.

class MenHome(ListView):
    model = men
    template_name = 'firstapp/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return men.objects.filter(is_published=True)

# def title(request):
#     ps = men.objects.all()
#     context = {
#         'title': 'Главная страница',
#         'top': ps,
#         'cat_selected': 0
#     }
#     return render(request, 'firstapp/index.html', context=context)


def about(request):
    return render(request, 'firstapp/about.html', {'title': 'О сайте', 'menu': menu})


def goroot(request):
    return redirect('root')

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'firstapp/addpage.html'
    success_url = reverse_lazy('root')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'

        return context
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('root')
#     else:
#         form = AddPostForm()
#     return render(request, 'firstapp/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


def contact(request):
    return HttpResponse('Оставьте сообщение')


def login(request):
    return HttpResponse('Ведите логин и пароль')


class ShowPost(DetailView):
    model = men
    template_name = 'firstapp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context
# def show_post(request, post_slug):
#     post = get_object_or_404(men, slug=post_slug)
#
#     context = {
#         'post': post,
#         'title': post.title,
#         'menu': menu,
#         'cat_selected': post.cat_id
#     }
#     return render(request, 'firstapp/post.html', context=context)



class MenCategory(ListView):
    model = Category
    template_name = 'firstapp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return men.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
# def show_category(request, cat_slug):
#     ps = men.objects.filter(cat__slug=cat_slug)
#     if len(ps) == 0:
#         raise Http404
#     context = {
#         'title': 'Отображение по рубрикам',
#         'posts': ps,
#         'menu': menu,
#         'cat_selected': cat_slug
#     }
#     return render(request, 'firstapp/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p>Вы ввели неизвестный для маршрутизатора запрос</p>')