# Generated by Django 5.1.2 on 2024-10-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestordeventas', '0018_alter_vendedores_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedores',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
