# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0016_exuserprofile_is_engineer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exuserprofile',
            name='is_engineer',
        ),
    ]
