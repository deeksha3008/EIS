# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accident_avoidance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinates',
            name='heart',
            field=models.CharField(default=100000, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordinates',
            name='ultra',
            field=models.CharField(default=100000, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordinates',
            name='x',
            field=models.CharField(default=100000, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordinates',
            name='y',
            field=models.CharField(default=100000, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordinates',
            name='z',
            field=models.CharField(default=100000, max_length=250),
            preserve_default=False,
        ),
    ]
