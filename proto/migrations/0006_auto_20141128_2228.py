# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0005_exuserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='engineer',
            field=models.CharField(default=1, max_length=30, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='call',
            name='logged_by',
            field=models.CharField(default=False, max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
