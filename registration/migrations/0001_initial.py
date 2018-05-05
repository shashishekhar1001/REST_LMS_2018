# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=128)),
                ('primary_registration_type', models.CharField(max_length=15, choices=[(b'Learner', b'Learner'), (b'Trainer', b'Trainer'), (b'Vendor', b'Vendor'), (b'Client', b'Client'), (b'Job Seeker', b'Job Seeker')])),
                ('secondary_registration_type', models.CharField(blank=True, max_length=15, choices=[(b'Learner', b'Learner'), (b'Trainer', b'Trainer'), (b'Vendor', b'Vendor'), (b'Client', b'Client'), (b'Job Seeker', b'Job Seeker')])),
                ('tertiary_registration_type', models.CharField(blank=True, max_length=15, choices=[(b'Learner', b'Learner'), (b'Trainer', b'Trainer'), (b'Vendor', b'Vendor'), (b'Client', b'Client'), (b'Job Seeker', b'Job Seeker')])),
                ('quaternary_registration_type', models.CharField(blank=True, max_length=15, choices=[(b'Learner', b'Learner'), (b'Trainer', b'Trainer'), (b'Vendor', b'Vendor'), (b'Client', b'Client'), (b'Job Seeker', b'Job Seeker')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
