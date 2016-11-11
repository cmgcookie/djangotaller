# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0004_infogeneral_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infogeneral',
            name='apellido',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='infogeneral',
            name='direccion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='infogeneral',
            name='estatura',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='infogeneral',
            name='fecha_nac',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infogeneral',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=2),
        ),
    ]
