# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_answer_options_quiz_quiz_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_question',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='module_referred',
            field=models.ForeignKey(related_name='quiz', to='registration.Course_Module'),
        ),
        migrations.AlterField(
            model_name='quiz_question',
            name='quiz',
            field=models.ForeignKey(related_name='questions', default=None, blank=True, to='registration.Quiz', null=True),
        ),
    ]
