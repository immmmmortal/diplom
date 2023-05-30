from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from my_site.models import Customer, Appointment, SalonService, Employee, RenderedService, User


@admin.register(Customer, Appointment, SalonService, RenderedService, User)
class AuthorAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(UserAdmin):
    model = Employee
    list_display = ('email', 'phone_number', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2'),
        }),
    )


admin.site.register(Employee, EmployeeAdmin)
