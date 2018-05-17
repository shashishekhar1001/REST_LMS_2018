# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20180516_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='no_of_ratings',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
