# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0022_auto_20150630_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='resolved',
        ),
        migrations.AddField(
            model_name='call',
            name='status',
            field=models.CharField(default=b'Unassigned', max_length=20, choices=[(b'Unassigned', b'Unassigned'), (b'Assigned', b'Assigned'), (b'Resolved', b'Resolved'), (b'Delayed', b'Delayed')]),
        ),
    ]
