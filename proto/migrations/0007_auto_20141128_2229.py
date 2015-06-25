# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0006_auto_20141128_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='engineer',
            field=models.CharField(default=False, max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='call',
            name='logged_by',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
