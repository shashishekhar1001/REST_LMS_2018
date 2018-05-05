# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20180427_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_module',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
