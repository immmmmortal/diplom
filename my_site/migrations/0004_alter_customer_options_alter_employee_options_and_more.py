# Generated by Django 4.2 on 2023-05-08 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0003_remove_customer_phone_number_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee'},
        ),
        migrations.AlterModelManagers(
            name='employee',
            managers=[
            ],
        ),
    ]
