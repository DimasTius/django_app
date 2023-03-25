from django.urls import path, re_path
from .views import sports, title, archive, goroot


urlpatterns = [
    path('',  title, name='root'),
    path('sport/<slug:sportid>/', sports),
    re_path(r'archive/(?P<year>\d{4})/$', archive),
    re_path(r'.*root/$', goroot)
]


