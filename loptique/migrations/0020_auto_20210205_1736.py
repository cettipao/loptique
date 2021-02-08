# Generated by Django 2.2 on 2021-02-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptique', '0019_auto_20210205_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='anteojo',
            name='precio_final_armazon',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='anteojo',
            name='precio_final_tratamientos',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]