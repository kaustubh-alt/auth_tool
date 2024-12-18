from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']  # Include phone field

        captcha = CaptchaField()
       
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number',
            }),
            
            
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
            }),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username',
        }),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
        }),
        label="Password"
    )
    captcha = CaptchaField()

from django import forms
from captcha.fields import CaptchaField


class CaptchaForm(forms.Form):
    catcha = CaptchaField()
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("Username","email","password1","password2")
