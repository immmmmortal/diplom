from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
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


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True, help_text=_('Required.'))
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Customer
        fields = ('email', 'phone')


class AppointmentChangeForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appointment_date'].widget.attrs.update({'class': 'form-control', 'type': 'datetime-local'})


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'readonly': True})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'readonly': True})
