# Generated by Django 5.0 on 2023-12-04 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_paises_continente_pais_pais_area_pais_capital_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='causa',
            name='Estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.estado'),
            preserve_default=False,
        ),
    ]
