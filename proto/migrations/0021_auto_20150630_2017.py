# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0020_auto_20150630_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=1, choices=[(1, b'1 - Poor'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5 - Average'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10 - Excellent')]),
        ),
    ]
