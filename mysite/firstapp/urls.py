from django.urls import path, re_path
from .views import title, about, goroot


urlpatterns = [
    path('',  title, name='root'),
    path('about/', about, name='about'),
    re_path('.*root/$', goroot)
]


