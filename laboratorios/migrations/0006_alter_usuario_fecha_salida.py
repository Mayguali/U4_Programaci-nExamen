# Generated by Django 3.2 on 2021-05-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0005_auto_20210521_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
    ]
