# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0003_call_resolved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='Resolved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
