from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from my_site.forms import CustomerCreationForm, CustomerLoginForm, UpdateUserForm
from my_site.models import Appointment


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
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'members/edit_profile.html', {'user_form': user_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'members/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')
