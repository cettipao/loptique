# Generated by Django 2.2 on 2021-02-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptique', '0027_auto_20210207_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]