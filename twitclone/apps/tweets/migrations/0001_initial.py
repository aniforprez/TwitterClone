# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tweet_text', models.CharField(max_length=140)),
                ('tweet_date', models.DateTimeField(verbose_name='tweet date')),
            ],
        ),
    ]
