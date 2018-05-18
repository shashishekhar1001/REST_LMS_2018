# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_auto_20180516_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner_model',
            name='courses_subscribed',
            field=models.ManyToManyField(to='registration.Course', null=True, blank=True),
        ),
    ]
