# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_course_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
    ]
