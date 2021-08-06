from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group',)

    def clean_subject(self):
        text = self.cleaned_data['text']
        group = self.cleaned_data['group']

        if text == "":
            raise forms.ValidationError('Без текста пост нельзя создать.')

        return text 