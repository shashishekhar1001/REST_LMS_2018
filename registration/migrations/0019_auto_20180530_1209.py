# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20180528_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnerQnA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chosen_option', models.ForeignKey(related_name='chosen_option', default=None, blank=True, to='registration.Answer_Options', null=True)),
                ('learner', models.ForeignKey(to='registration.Learner_Model')),
                ('quiz_question', models.ForeignKey(to='registration.Quiz_Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='learnerquestionanswer',
            name='chosen_option',
        ),
        migrations.RemoveField(
            model_name='learnerquestionanswer',
            name='learner',
        ),
        migrations.RemoveField(
            model_name='learnerquestionanswer',
            name='quiz_question',
        ),
        migrations.DeleteModel(
            name='LearnerQuestionAnswer',
        ),
    ]
