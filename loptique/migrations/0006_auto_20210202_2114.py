# Generated by Django 2.2 on 2021-02-03 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loptique', '0005_auto_20210202_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loptique.Paciente'),
        ),
    ]