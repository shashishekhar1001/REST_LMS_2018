# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_trainer_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learner_Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_picture', models.ImageField(upload_to=b'profile_pics/%Y/%m/%d/', blank=True)),
                ('courses_learning', models.TextField()),
                ('user', models.ForeignKey(to='registration.Custom_User')),
            ],
        ),
    ]
