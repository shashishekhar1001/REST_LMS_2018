# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_auto_20180802_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learner_model',
            name='courses_learning',
        ),
    ]
