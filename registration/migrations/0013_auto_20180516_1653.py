# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_course_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='no_of_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
