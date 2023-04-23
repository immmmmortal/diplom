from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from members import views

urlpatterns = [
                path('signup/', views.SignUpView.as_view(), name='signup'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL)
