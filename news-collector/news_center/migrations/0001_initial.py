# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('url', models.CharField(max_length=1024, verbose_name='\u6765\u6e90\u5730\u5740')),
                ('nid', models.CharField(max_length=30, verbose_name='nid')),
                ('site', models.CharField(max_length=30, null=True, verbose_name='\u6765\u6e90\u5a92\u4f53')),
                ('ts', models.CharField(max_length=30, null=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('b_type', models.CharField(max_length=30, null=True, verbose_name='\u7c7b\u578b')),
                ('imageurls', models.CharField(max_length=1024, null=True, verbose_name='\u56fe\u7247')),
                ('n_abs', models.CharField(max_length=100, null=True, verbose_name='\u539f\u6807\u9898')),
                ('n_date', models.DateField(verbose_name='\u65e5\u671f', db_index=True)),
            ],
            options={
                'db_table': 'news',
                'verbose_name': '\u65b0\u95fb',
                'verbose_name_plural': '\u65b0\u95fb',
            },
        ),
    ]
