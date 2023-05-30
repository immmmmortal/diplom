from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from my_site.forms import CustomerCreationForm, CustomerLoginForm, UpdateUserForm
from my_site.models import Appointment, User, RenderedService, Employee
from datetime import datetime


def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        # Check if the user is a customer
        customer = authenticate(request, email=email, password=password)
        if customer is not None:
            login(request, customer)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')

        # Check if the user is an employee
        employee = authenticate(request, email=email, password=password)
        if employee is not None:
            login(request, employee)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')

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
    user: User = request.user
    current_date = datetime.now().date()
    if user.is_employee():
        upcoming_appointments = Appointment.objects.filter(appointment_date__gte=current_date)
        booked_times_in_appointments = RenderedService.objects.filter(employee_id=user.id)
        past_appointments = RenderedService.objects.filter(employee_id=user.id)

        available_appointments = upcoming_appointments.exclude(
            id__in=booked_times_in_appointments.values_list('appointment_id__id', flat=True)
        ).exclude(
            appointment_date__in=past_appointments.values_list('appointment_id__appointment_date', flat=True),
            appointment_time__in=past_appointments.values_list('appointment_id__appointment_time', flat=True)
        )

        context = {
            'appointments': available_appointments,
            'past_appointments': past_appointments,

        }
        if request.method == 'POST':
            RenderedService.objects.create(
                employee_id=Employee.objects.get(pk=user.id),
                appointment_id=Appointment.objects.get(pk=request.POST.get('appointment_id'))
            )
            messages.success(request, 'Accepted appointment successfully.')

        return render(request, 'members/employee_profile.html', context)
    else:
        user = request.user
        upcoming_appointments = Appointment.objects.filter(customer=user, appointment_date__gte=current_date)
        past_appointments = Appointment.objects.filter(customer=user, appointment_date__lt=current_date)
        if request.method == 'POST':
            appointment_id = request.POST.get('appointment_id')
            if appointment_id:
                appointment = get_object_or_404(Appointment, pk=appointment_id)
                appointment.delete()
                messages.success(request, 'Appointment cancelled successfully.')

        context = {
            'user': user,
            'appointments': upcoming_appointments,
            'past_appointments': past_appointments,
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
