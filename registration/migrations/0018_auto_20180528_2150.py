# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_learnerquestionanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner_model',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'profile_pics/%Y/%m/%d/', blank=True),
        ),
    ]
