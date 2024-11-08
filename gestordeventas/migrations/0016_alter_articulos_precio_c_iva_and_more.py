# Generated by Django 5.1.2 on 2024-10-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestordeventas', '0015_rename_precio_unitario_ventas_total_venta_c_iva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='precio_c_iva',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='precio_s_iva',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='total_venta_c_iva',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='total_venta_s_iva',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
