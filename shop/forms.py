from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Messages
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'name',
            'email': 'e-mail',
            'message': 'message'
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 7, 'cols': 60})
        }


class RegistrationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginForm(AuthenticationForm):

    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class ServiceForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Defects
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 80})
        }
        labels = {
            'email': 'e-mail',
            'name': 'name',
            'phone': 'phone',
            'description': 'description',
        }


class AddGoodForm(forms.Form):
    quantity = forms.IntegerField()


class CartForm(forms.Form):
    phone = forms.CharField()
    delivery_address = forms.CharField()


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()
    captcha = CaptchaField()


