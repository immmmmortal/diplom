from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from my_site.forms import AppointmentForm, DateForm, TIME_CHOICES
from my_site.models import SalonService, Appointment
import datetime


def home(request):
    services = SalonService.objects.all()
    return render(request, 'my_site/home.html', {'services': services})


def service_booking(request, pk):
    service = get_object_or_404(SalonService, pk=pk)
    if request.method == 'POST':
        date_form = DateForm(request.POST)
        if date_form.is_valid():
            Appointment.objects.create(customer=request.user,
                                       service=service,
                                       appointment_date=date_form.cleaned_data['appointment_date'],
                                       appointment_time=request.POST.get('appointment_time')
                                       )
            messages.success(request, 'Your appointment has been booked!')
            print(request.session['messages'])  # add this line
            return render(request, 'my_site/service_detail.html', {
                'service': service,
                'date_form': date_form,
            })
        else:
            appointment_form = AppointmentForm()
            return render(request, 'my_site/service_detail.html', {
                'date_form': date_form,
                'service': service,
                'appointment_form': appointment_form,
            })
    else:
        appointment_form = AppointmentForm()
        return render(request, 'my_site/service_detail.html', {
            'date_form': DateForm(),
            'service': service,
            'appointment_form': appointment_form,
        })


def get_available_times(request):
    selected_date = request.POST.get('appointment_date')
    existing_appointments = Appointment.objects.filter(appointment_date=selected_date)
    available_times = [(choice[0], choice[1]) for choice in TIME_CHOICES
                       if datetime.datetime.strptime(choice[0],
                                                     '%H:%M:%S').time() not in existing_appointments.values_list(
            'appointment_time', flat=True)]
    return JsonResponse(available_times, safe=False)


def about(request):
    return render(request, 'my_site/about.html')


def logout_view(request):
    logout(request)
    return redirect('signup')
