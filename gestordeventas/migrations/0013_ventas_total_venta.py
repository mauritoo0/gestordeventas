# Generated by Django 5.1.2 on 2024-10-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestordeventas', '0012_alter_clientes_vendedor_alter_ventas_articulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='total_venta',
            field=models.FloatField(null=True),
        ),
    ]