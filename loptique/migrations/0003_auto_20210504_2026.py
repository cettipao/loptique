# Generated by Django 2.2 on 2021-05-04 23:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptique', '0002_auto_20210504_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[^$)]+$', "No puede contener '$' ni ')'.")]),
        ),
    ]
