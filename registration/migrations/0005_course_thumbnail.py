# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_course_course_module_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(upload_to=b'Course_Thumbnails/%Y/%m/%d/', blank=True),
        ),
    ]
