# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20180323_1826'),
        ('blog_and_comments', '0005_auto_20180327_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created', '-updated']},
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(related_name='blog_likes', to='registration.Custom_User', blank=True),
        ),
    ]
