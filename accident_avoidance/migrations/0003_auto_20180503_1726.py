# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accident_avoidance', '0002_auto_20180406_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinates',
            name='smoke',
            field=models.CharField(default=1000, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordinates',
            name='speed',
            field=models.CharField(default=1000, max_length=250),
            preserve_default=False,
        ),
    ]
