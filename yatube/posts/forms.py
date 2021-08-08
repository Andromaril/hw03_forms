from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        text = forms.CharField()
        group = forms.CharField()
        fields = ('text', 'group',)
        help_texts = {
            'text': 'Тут пишите текст поста',
            'group': 'Тут выбираете группу, к которой принадлежит пост',
        }
