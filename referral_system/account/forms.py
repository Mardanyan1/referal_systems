from django import forms
from django.contrib.auth.models import User


# class RegistrationForm(forms.ModelForm):
#     phone_number = forms.CharField(label='Phone number', max_length=11, widget=forms.TextInput)  # Максимальная длина номера телефона - 11 символов
#     password = forms.CharField(label='Password', max_length=4, widget=forms.PasswordInput())  # Пароль из 4 символов
#
#     class Meta:
#         model = User
#         fields = ['phone_number', 'password']  # Поля для ввода
#
#
# class RegistrationPhoneForm(forms.Form):
#     phone_number = forms.CharField(label='Phone number', max_length=11, widget=forms.TextInput)
#
#
# class RegistrationPasswordForm(forms.Form):
#     password = forms.CharField(label='Password', max_length=4, widget=forms.PasswordInput())  # Пароль из 4 символов