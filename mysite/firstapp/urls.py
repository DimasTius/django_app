from django.urls import path, re_path
from .views import title, about, goroot, login, addpage, contact, show_post


urlpatterns = [
    path('',  title, name='root'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    re_path(r'.*root/$', goroot)
]


