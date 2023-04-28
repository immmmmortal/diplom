from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .models import Customer, Appointment
from django.utils.translation import gettext_lazy as _


class CustomerCreationForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone_number', 'password1', 'password2')


class CustomerLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=255,
                                widget=forms.EmailInput(attrs={'autofocus': True, 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UpdateUserForm(forms.ModelForm):
    name = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=20,
                                   required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number']


