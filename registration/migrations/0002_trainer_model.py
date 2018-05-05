# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer_Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('profile_picture', models.ImageField(upload_to=b'profile_pics/%Y/%m/%d/', blank=True)),
                ('courses_tutoring', models.TextField()),
                ('describe_yourself', models.TextField()),
                ('linked_in_url', models.URLField()),
                ('skills', models.TextField(blank=True)),
                ('cv', models.FileField(upload_to=b'cvs/%Y/%m/%d/', blank=True)),
                ('user', models.ForeignKey(to='registration.Custom_User')),
            ],
        ),
    ]
