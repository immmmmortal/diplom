from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from datetime import datetime

from my_site.models import SalonService, Appointment


def home(request):
    services = SalonService.objects.all()
    return render(request, 'my_site/home.html', {'services': services})


def service_detail(request, service_id):
    service = get_object_or_404(SalonService, pk=service_id)
    return render(request, 'my_site/service_detail.html', {'service': service})


@require_POST
def create_appointment(request, service_id):
    appointment_date_time = request.POST['appointment_date_time']
    service_id = service_id
    customer_id = request.POST['customer_id']

    # Check if the appointment time is available for the selected service
    if not Appointment.objects.filter(service_id=service_id,
                                      appointment_date=datetime.strptime(appointment_date_time, '%Y-%m-%dT%H:%M')):
        # Create a new appointment record
        appointment = Appointment(
            appointment_date=appointment_date_time,
            customer_id=customer_id,
            service_id=service_id
        )
        appointment.save()
        messages.success(request, 'Appointment created successfully.')
    else:
        messages.error(request, 'The selected time is already taken for this service.')

    return redirect('service_details', id=service_id)


def about(request):
    return render(request, 'my_site/about.html')


def logout_view(request):
    logout(request)
    return redirect('signup')
