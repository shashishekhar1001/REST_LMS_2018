# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_and_comments', '0003_auto_20180327_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
