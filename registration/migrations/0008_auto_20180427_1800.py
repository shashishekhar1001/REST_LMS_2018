# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20180410_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_module',
            name='Assignment',
            field=models.FileField(null=True, upload_to=registration.models.content_assignmentfile_name, blank=True),
        ),
        migrations.AlterField(
            model_name='course_module',
            name='Presentation',
            field=models.FileField(null=True, upload_to=registration.models.content_pptfile_name, blank=True),
        ),
        migrations.AlterField(
            model_name='course_module',
            name='topics',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course_module',
            name='video',
            field=models.FileField(null=True, upload_to=registration.models.content_videofile_name, blank=True),
        ),
    ]
