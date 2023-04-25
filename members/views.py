from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from my_site.forms import CustomerCreationForm, CustomerLoginForm, CustomUserChangeForm, AppointmentChangeForm, \
    CustomUserForm
from my_site.models import Appointment, RenderedService, Customer


def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid email or password'
            return render(request, 'members/login.html', {'error': error})
    else:
        form = CustomerLoginForm()
        return render(request, 'members/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(request, email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'], )
            if new_user:
                login(request, new_user)
                return redirect('home')
    else:
        form = CustomerCreationForm()
    return render(request, 'members/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    user = request.user
    appointments = Appointment.objects.filter(customer=user)

    context = {
        'user': user,
        'appointments': appointments,

    }

    return render(request, 'members/profile.html', context)


@login_required
def edit_profile(request):
    pass
