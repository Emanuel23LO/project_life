# Generated by Django 5.0.1 on 2024-01-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
