from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer, Appointment, RenderedService
from datetime import date

TIME_CHOICES = (
    ('12:00:00', '12am'),
    ('13:00:00', '1pm'),
    ('14:00:00', '2pm'),
    ('15:00:00', '3pm'),
    ('16:00:00', '4pm'),
    ('17:00:00', '5pm'),
)


class CustomerCreationForm(UserCreationForm):
    username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = Customer
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


class CustomerLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=255,
                                widget=forms.EmailInput(attrs={'autofocus': True, 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=20,
                                   required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ['username', 'email', 'phone_number']






class DateForm(forms.Form):
    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}), initial=None)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_time']
        widgets = {
            'appointment_time': forms.Select(choices=[])
        }


