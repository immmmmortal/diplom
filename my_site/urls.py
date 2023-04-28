from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name='home'),
                  path('about/', views.about, name='about'),
                  path('logout/', views.logout_view, name='logout'),
                  path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
                  path('create_appointment/', views.CreateAppointmentView.as_view(), name='create_appointment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL)
