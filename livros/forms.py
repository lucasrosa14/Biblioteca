from django import forms
from .models import Book, UserProfile


class LivroForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'capa', 'capa_url']

class SimpleUserCreationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    sexo = forms.ChoiceField(choices=UserProfile.SEXO_CHOICES)
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))