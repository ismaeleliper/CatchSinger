from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User


# Formulário  básico de usuário.
class UserForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Digite seu Email'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Apelido'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Crie sua senha'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic',)
        labels = {
            'profile_pic': '',
        }

# Formulário de informações adcionais sobre o usuário.

# Todo: Criar campos adcionais, especificados no projeto.