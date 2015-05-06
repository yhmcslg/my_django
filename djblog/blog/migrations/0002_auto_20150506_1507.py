# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u6587\u7ae0\u5206\u7c7b')),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='po_type',
            field=models.ForeignKey(verbose_name='\u6587\u7ae0\u5206\u7c7b', blank=True, to='blog.Category', null=True),
            preserve_default=True,
        ),
    ]
