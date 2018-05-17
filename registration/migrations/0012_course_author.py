# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20180503_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
