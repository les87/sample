# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proto', '0009_auto_20141128_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
