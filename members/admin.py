from django.contrib import admin

from my_site.models import Customer, Appointment, SalonService, Employee


@admin.register(Customer, Appointment, SalonService, Employee)
class AuthorAdmin(admin.ModelAdmin):
    pass


