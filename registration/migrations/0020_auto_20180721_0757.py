# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20180530_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='Course_Thumbnails/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='primary_registration_type',
            field=models.CharField(max_length=15, choices=[('Learner', 'Learner'), ('Trainer', 'Trainer'), ('Vendor', 'Vendor'), ('Client', 'Client'), ('Job Seeker', 'Job Seeker')]),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='quaternary_registration_type',
            field=models.CharField(max_length=15, blank=True, choices=[('Learner', 'Learner'), ('Trainer', 'Trainer'), ('Vendor', 'Vendor'), ('Client', 'Client'), ('Job Seeker', 'Job Seeker')]),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='secondary_registration_type',
            field=models.CharField(max_length=15, blank=True, choices=[('Learner', 'Learner'), ('Trainer', 'Trainer'), ('Vendor', 'Vendor'), ('Client', 'Client'), ('Job Seeker', 'Job Seeker')]),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='tertiary_registration_type',
            field=models.CharField(max_length=15, blank=True, choices=[('Learner', 'Learner'), ('Trainer', 'Trainer'), ('Vendor', 'Vendor'), ('Client', 'Client'), ('Job Seeker', 'Job Seeker')]),
        ),
        migrations.AlterField(
            model_name='learner_model',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='trainer_model',
            name='cv',
            field=models.FileField(blank=True, upload_to='cvs/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='trainer_model',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pics/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='course',
            field=models.ForeignKey(to='registration.Course'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='learner',
            field=models.ForeignKey(to='registration.Learner_Model'),
        ),
    ]
