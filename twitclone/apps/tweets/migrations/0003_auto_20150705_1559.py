# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20150705_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
