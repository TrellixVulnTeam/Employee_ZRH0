# Generated by Django 2.1.3 on 2018-11-12 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApi', '0002_auto_20181112_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='startDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
