# Generated by Django 5.1.2 on 2024-10-10 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestordeventas', '0002_articulos'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedores',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestordeventas.articulos')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestordeventas.vendedores')),
            ],
        ),
    ]