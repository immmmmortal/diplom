# Generated by Django 4.2 on 2023-04-28 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0003_customer_groups_customer_is_active_customer_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='duration',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
