# Generated by Django 4.2.10 on 2024-02-27 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
    ]
