# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0010_auto_20141129_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='user',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
    ]
