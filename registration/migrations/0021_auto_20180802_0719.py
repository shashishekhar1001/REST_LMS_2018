# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0020_auto_20180721_0757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'permissions': (('access_course', 'Access Course'),)},
        ),
    ]
