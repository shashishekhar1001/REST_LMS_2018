# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_remove_learner_model_courses_learning'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_module',
            name='allow_preview',
            field=models.NullBooleanField(default=False),
        ),
    ]
