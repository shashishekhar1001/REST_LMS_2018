# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_learner_model_courses_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_module',
            name='Refernce',
            field=models.FileField(null=True, upload_to=registration.models.content_referencefile_name, blank=True),
        ),
    ]
