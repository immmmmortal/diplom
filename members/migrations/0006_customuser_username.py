# Generated by Django 4.2 on 2023-04-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_remove_customuser_username_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
