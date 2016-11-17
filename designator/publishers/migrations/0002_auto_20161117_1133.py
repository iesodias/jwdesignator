# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Publicador', 'verbose_name_plural': 'Publicadores'},
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=100, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='car',
            field=models.CharField(max_length=30, verbose_name='carrinho'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='designation',
            field=models.CharField(max_length=30, verbose_name='designacao'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='gender',
            field=models.CharField(max_length=30, verbose_name='sexo'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='group',
            field=models.CharField(max_length=30, verbose_name='grupo'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='telefone'),
        ),
    ]
