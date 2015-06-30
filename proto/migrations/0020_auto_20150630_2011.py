# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0019_call_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='category',
            field=models.CharField(default=b'<Category Not Selected>', max_length=2, choices=[(b'PS', b'Printer Setup'), (b'PJ', b'Printer Jam'), (b'NT', b'No Toner'), (b'PP', b'Power Problem'), (b'EC', b'Error Code'), (b'OT', b'Other')]),
        ),
    ]
