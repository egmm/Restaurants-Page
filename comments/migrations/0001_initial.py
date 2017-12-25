# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    #dependencies = [
    #    ('list', '0001_initial'),
    #]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Restaurant')),
            ],
        ),
    ]
