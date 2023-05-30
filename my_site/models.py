from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


class EmployeeManager(BaseUserManager):
    def create_user(self, email, name, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password, **extra_fields):
        user = self.create_user(
            email=email,
            name=name,
            phone_number=phone_number,
            password=password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomerManager(BaseUserManager):
    def create_user(self, email, name, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password):
        user = self.create_user(
            email=email,
            name=name,
            phone_number=phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = 'CU', 'Customer'
        EMPLOYEE = 'EM', 'Employee'

    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    base_role = Role.CUSTOMER
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'phone_number']

    def is_employee(self):
        return self.role == self.Role.EMPLOYEE

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class Employee(User):
    base_role = User.Role.EMPLOYEE
    objects = EmployeeManager()

    class Meta:
        verbose_name = 'Employee'

    def __str__(self):
        return self.email


class Customer(User):
    base_role = User.Role.CUSTOMER
    objects = CustomerManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Customer'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class SalonService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Appointment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(SalonService, on_delete=models.CASCADE)
    appointment_date = models.DateField(auto_created=True)
    appointment_time = models.TimeField(auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('service', 'appointment_date', 'customer', 'appointment_time')


class RenderedService(models.Model):
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
