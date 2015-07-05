# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0023_auto_20150701_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='deadline',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
