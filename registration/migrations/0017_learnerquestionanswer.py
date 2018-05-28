# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_course_module_refernce'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnerQuestionAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chosen_option', models.ForeignKey(related_name='chosen_option', default=None, blank=True, to='registration.Answer_Options', null=True)),
                ('learner', models.ForeignKey(to='registration.Learner_Model')),
                ('quiz_question', models.ForeignKey(to='registration.Quiz_Question')),
            ],
        ),
    ]
