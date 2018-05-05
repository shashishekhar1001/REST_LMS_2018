# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_and_comments', '0004_remove_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to=b'blog_pics/%Y/%m/%d/', blank=True),
        ),
    ]
