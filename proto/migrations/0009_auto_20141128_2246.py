# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0008_auto_20141128_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='call',
            old_name='Resolved',
            new_name='resolved',
        ),
    ]
