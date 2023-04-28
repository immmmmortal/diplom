from django.utils import timezone
from datetime import timedelta
from django.core import serializers
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView
from my_site.models import SalonService, Appointment


def home(request):
    services = SalonService.objects.all()
    return render(request, 'my_site/home.html', {'services': services})


def service_detail(request, service_id):
    service = get_object_or_404(SalonService, pk=service_id)
    return render(request, 'my_site/service_detail.html', {'service': service})


class ServiceDetailView(DetailView):
    model = SalonService
    template_name = 'my_site/service_detail.html'


class CreateAppointmentView(View):
    pass


def about(request):
    return render(request, 'my_site/about.html')


def logout_view(request):
    logout(request)
    return redirect('signup')
