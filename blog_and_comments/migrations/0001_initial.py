# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20180323_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(height_field=b'height_field', width_field=b'width_field', upload_to=b'blog_pics/%Y/%m/%d/', blank=True)),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('blogger', models.ForeignKey(to='registration.Custom_User')),
            ],
        ),
    ]
