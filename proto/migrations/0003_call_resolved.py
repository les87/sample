# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0002_auto_20141121_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='Resolved',
            field=models.BooleanField(default=b'False'),
            preserve_default=True,
        ),
    ]
