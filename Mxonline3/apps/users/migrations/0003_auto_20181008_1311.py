# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181007_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图管理', 'verbose_name_plural': '轮播图管理'},
        ),
    ]