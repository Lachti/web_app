# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-29 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_book_is_rented'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]