# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_course_module_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_Options',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Answer Option',
                'verbose_name_plural': 'Answer Options',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quiz_name', models.CharField(max_length=200)),
                ('module_referred', models.ForeignKey(to='registration.Course_Module')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizes',
            },
        ),
        migrations.CreateModel(
            name='Quiz_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q_type', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=200)),
                ('correct', models.ForeignKey(related_name='correct', default=None, blank=True, to='registration.Answer_Options', null=True)),
                ('possible_answers', models.ManyToManyField(to='registration.Answer_Options')),
                ('quiz', models.ForeignKey(default=None, blank=True, to='registration.Quiz', null=True)),
                ('selected', models.ForeignKey(related_name='selected', default=None, blank=True, to='registration.Answer_Options', null=True)),
            ],
            options={
                'verbose_name': 'Quiz Question',
                'verbose_name_plural': 'Quiz Questions',
            },
        ),
    ]
