from django import forms
from .models import men, Category

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    slug = forms.SlugField(max_length=100, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Контент')
    is_published = forms.BooleanField(label='Публикация', initial=True, required=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана')