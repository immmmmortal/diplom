from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from members import views

urlpatterns = [
                  path('signup/', views.signup_view, name='signup'),
                  path('login/', views.login_view, name='login'),
                  path('logout/', views.logout_view, name='logout'),
                  path('profile/', views.profile, name='profile'),
                  path('edit_profile/', views.edit_profile, name='edit_profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL)
