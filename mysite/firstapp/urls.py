from django.urls import path
from .views import index, onepage

urlpatterns = [
    path('',  index),
    path('pagefirstapp/', onepage)
]