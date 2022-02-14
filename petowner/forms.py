# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Kullanıcı Adı', required=False, help_text='Optional.')
    first_name = forms.CharField(max_length=30, label='Ad', required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, label='Soyad', required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, label='E-posta', help_text='Required. Inform a valid email address.')

    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolalar eşleşmiyor!")

        return password2


class ProfileForm(forms.ModelForm):
    phone = forms.CharField(max_length=15, required=False, label='Telefon', help_text='Optional.')

    class Meta:
        model = Profile
        fields = ('phone',)


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'password']



