# Generated by Django 2.2 on 2021-02-04 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loptique', '0008_auto_20210203_2205'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cuotas',
            new_name='Cuota',
        ),
        migrations.RenameModel(
            old_name='Varios',
            new_name='Venta_varios',
        ),
        migrations.AlterModelOptions(
            name='anteojocerca',
            options={'verbose_name_plural': 'Anteojos Cerca'},
        ),
        migrations.AlterModelOptions(
            name='anteojolejos',
            options={'verbose_name_plural': 'Anteojos Lejos'},
        ),
        migrations.AlterModelOptions(
            name='armazon',
            options={'verbose_name_plural': 'armazones'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': 'colores'},
        ),
        migrations.AlterModelOptions(
            name='formadepago',
            options={'verbose_name_plural': 'Formas De Pago'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name_plural': 'materiales'},
        ),
        migrations.AlterModelOptions(
            name='multifocal',
            options={'verbose_name_plural': 'multifocales'},
        ),
        migrations.AlterModelOptions(
            name='obra_social',
            options={'verbose_name_plural': 'Obras Sociales'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name_plural': 'proveedores'},
        ),
        migrations.AlterModelOptions(
            name='tipo_multifocal',
            options={'verbose_name_plural': 'Tipos Multifocal'},
        ),
        migrations.AlterModelOptions(
            name='venta_varios',
            options={'verbose_name_plural': 'Ventas Varios'},
        ),
    ]