# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_and_comments', '0002_auto_20180327_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish',
            field=models.DateField(null=True, blank=True),
        ),
    ]
