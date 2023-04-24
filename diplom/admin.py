from django.contrib import admin
from members.models import CustomUser
from my_site.models import Customer, Employee, Appointment, SalonService


@admin.register(Customer, Employee, Appointment, SalonService,CustomUser)
class PersonAdmin(admin.ModelAdmin):
    pass
