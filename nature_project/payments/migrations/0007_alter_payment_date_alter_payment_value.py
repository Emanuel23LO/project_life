# Generated by Django 4.2.10 on 2024-02-27 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_alter_payment_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='payment',
            name='value',
            field=models.FloatField(max_length=500),
        ),
    ]