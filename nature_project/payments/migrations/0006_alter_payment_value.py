# Generated by Django 4.2.10 on 2024-02-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_payment_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='value',
            field=models.FloatField(max_length=50),
        ),
    ]
