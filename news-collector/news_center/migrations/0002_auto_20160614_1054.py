# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='ts',
            field=models.DateField(null=True, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]
