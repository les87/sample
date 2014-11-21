# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True)),
                ('engineer_comment', models.TextField()),
                ('logged_by', models.CharField(max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('call', models.ForeignKey(to='proto.Call')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number', models.CharField(unique=True, max_length=200)),
                ('asset_tag', models.CharField(unique=True, max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('ip_address', models.GenericIPAddressField(unpack_ipv4=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='call',
            name='printer',
            field=models.ForeignKey(to='proto.Printer'),
            preserve_default=True,
        ),
    ]
