# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0002_student_g_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'good_user',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='g_user',
            field=models.ManyToManyField(to='stu.GoodsUser'),
        ),
    ]
