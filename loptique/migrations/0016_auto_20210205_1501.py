# Generated by Django 2.2 on 2021-02-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptique', '0015_auto_20210204_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='anteojo',
            name='precio_armazon',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='anteojo',
            name='precio_final_armazon',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='anteojo',
            name='precio_final_lente',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='anteojo',
            name='precio_final_tratamientos',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='anteojo',
            name='precio_lente',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='anteojo',
            name='precio_tratamientos',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
