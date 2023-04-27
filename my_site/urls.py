from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name='home'),
                  path('about/', views.about, name='about'),
                  path('logout/', views.logout_view, name='logout'),
                  path('services/<int:service_id>/', views.service_detail, name='service_detail'),
                  path('services/<int:pk>/create_appointment/', views.create_appointment, name='create_appointment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL)
