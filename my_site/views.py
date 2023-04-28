from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView

from my_site.models import SalonService, Appointment, Customer


def home(request):
    services = SalonService.objects.all()
    return render(request, 'my_site/home.html', {'services': services})


def service_detail(request, service_id):
    service = get_object_or_404(SalonService, pk=service_id)
    return render(request, 'my_site/service_detail.html', {'service': service})


class ServiceDetailView(DetailView):
    model = SalonService
    template_name = 'my_site/service_detail.html'


def create_appointment(request):
    if request.method == 'POST':
        appointment_date_time = request.POST['appointment_date_time']
        service_id = request.POST['service_id']
        customer_id = request.POST['customer_id']

        # Check if appointment is already booked for the same date and time for the same service
        if Appointment.objects.filter(appointment_date_time=appointment_date_time, service_id=service_id).exists():
            return HttpResponse('Appointment already booked for the selected date and time for this service.')

        # Check if there is another appointment for the same service at the selected date and time
        if Appointment.objects.filter(appointment_date_time=appointment_date_time, service_id=service_id).exists():
            return HttpResponse('Another appointment already booked for the selected date and time for this service.')

        # Create a new appointment object and save it to the database
        appointment = Appointment(appointment_date_time=appointment_date_time, service_id=service_id,
                                  customer_id=customer_id)
        appointment.save()

        return redirect('appointment_confirmation')

    else:
        # Render the create appointment form with the available services and customers
        services = SalonService.objects.all()
        customers = Customer.objects.all()
        context = {'services': services, 'customers': customers}
        return render(request, 'my_site/create_appointment.html', context)


def about(request):
    return render(request, 'my_site/about.html')


def logout_view(request):
    logout(request)
    return redirect('signup')
