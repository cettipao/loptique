# Generated by Django 2.2 on 2021-02-03 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptique', '0004_auto_20210202_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='seña',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
