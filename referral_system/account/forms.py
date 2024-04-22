from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone number', max_length=11)  # Максимальная длина номера телефона - 11 символов
    auth_code = forms.CharField(label='Password', max_length=4, widget=forms.PasswordInput())  # Пароль из 4 символов

    class Meta:
        model = User
        fields = ['phone_number', 'auth_code']  # Поля для ввода
