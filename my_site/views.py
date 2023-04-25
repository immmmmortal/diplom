from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'my_site/home.html')


def about(request):
    return render(request, 'my_site/about.html')


def logout_view(request):
    logout(request)
    return redirect('home')



