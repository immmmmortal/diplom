from django.utils import timezone
from datetime import timedelta
from django.core import serializers
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView

from my_site.forms import AppointmentForm
from my_site.models import SalonService, Appointment


def home(request):
    services = SalonService.objects.all()
    return render(request, 'my_site/home.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(SalonService, pk=pk)
    return render(request, 'my_site/service_detail.html', {'service': service})





def about(request):
    return render(request, 'my_site/about.html')


def logout_view(request):
    logout(request)
    return redirect('signup')
