# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0007_auto_20141128_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='engineer',
            field=models.CharField(default=b'No Engineer Assigned', max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
