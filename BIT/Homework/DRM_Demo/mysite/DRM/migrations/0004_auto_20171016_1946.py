# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DRM', '0003_auto_20171013_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='key',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='ebook',
            field=models.FileField(upload_to='ebook'),
        ),
    ]
