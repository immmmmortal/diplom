from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name='home'),
                  path('about/', views.about, name='about'),
                  path('logout/', views.logout_view, name='logout'),
                  path('services/<int:pk>/', views.service_booking, name='service_booking'),
                  path('get_available_times/', views.get_available_times, name='get_available_times'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL)
