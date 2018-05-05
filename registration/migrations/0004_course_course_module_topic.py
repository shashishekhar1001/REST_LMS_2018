# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_learner_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prerequisite', models.TextField()),
                ('requirements', models.TextField()),
                ('course_by', models.ForeignKey(to='registration.Trainer_Model')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to=registration.models.content_videofile_name, blank=True)),
                ('Presentation', models.FileField(upload_to=registration.models.content_pptfile_name, blank=True)),
                ('Assignment', models.FileField(upload_to=registration.models.content_assignmentfile_name, blank=True)),
                ('topics', models.TextField()),
                ('part_of', models.ForeignKey(to='registration.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic_name', models.CharField(max_length=200)),
                ('part_of', models.ForeignKey(to='registration.Course_Module')),
            ],
        ),
    ]
