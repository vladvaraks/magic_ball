from django.contrib.auth import authenticate
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-login-form',
        'placeholder': 'Представся шару',
    }))     

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)


    def clean(self):
        username = self.cleaned_data.get('username')
        self.user_cache = authenticate(self.request, username=username)
        return self.cleaned_data
    
    def get_user(self):
        return self.user_cache


class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-login-form',
        'placeholder': 'Задай вопрос',
    }))

    def clean_question(self):
        question = self.cleaned_data.get('question').lower()
        question = ' '.join(question.split())
        if not question:
             raise forms.ValidationError('Введите ваш вопрос')
        return question

    def clean(self):
        return self.cleaned_data