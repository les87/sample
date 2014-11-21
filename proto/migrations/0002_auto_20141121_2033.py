# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='call',
            name='engineer_comment',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='call',
            name='logged_by',
            field=models.CharField(default=1, max_length=30, blank=True),
            preserve_default=False,
        ),
    ]
