# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20180323_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_module',
            name='part_of',
            field=models.ForeignKey(related_name='modules', to='registration.Course'),
        ),
    ]
