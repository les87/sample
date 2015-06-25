# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0013_remove_exuserprofile_is_engineer'),
    ]

    operations = [
        migrations.AddField(
            model_name='exuserprofile',
            name='is_engineer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
