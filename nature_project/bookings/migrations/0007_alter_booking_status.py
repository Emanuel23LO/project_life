from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_merge_20240201_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Reservado'), (5, 'Anulada'), (4, 'En Ejecucion'), (2, 'Por Confirmar'), (3, 'Confirmado')], default=1),

        ),
    ]
