# Generated by Django 5.1.2 on 2024-10-10 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestordeventas', '0004_alter_ventas_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendedores',
            old_name='vendedor',
            new_name='nombre',
        ),
    ]
