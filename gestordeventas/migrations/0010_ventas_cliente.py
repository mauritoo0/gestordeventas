# Generated by Django 5.1.2 on 2024-10-12 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestordeventas', '0009_alter_clientes_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestordeventas.clientes'),
            preserve_default=False,
        ),
    ]
