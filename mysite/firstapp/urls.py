from django.urls import path, re_path
from .views import MenHome, about, goroot, login, AddPage, contact, ShowPost, MenCategory


urlpatterns = [
    path('',  MenHome.as_view(), name='root'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MenCategory.as_view(), name='category'),
    re_path(r'.*root/$', goroot)
]


