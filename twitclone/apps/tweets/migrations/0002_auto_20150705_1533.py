# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ('-tweet_date',)},
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_user',
            field=models.CharField(max_length=100, default=2),
            preserve_default=False,
        ),
    ]
