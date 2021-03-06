# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-22 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investorBp', '0003_investor_ps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='company',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='create_time',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='email',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='fields',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='industry',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='investAmount',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='last_login',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='position',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='realname',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='roles',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='stages',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='telephone',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='the_id',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='update_time',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='investor',
            name='weixin',
            field=models.CharField(max_length=300),
        ),
    ]
