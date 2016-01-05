# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_newsplus', '0002_auto_20150428_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsimage',
            name='size_h',
            field=models.PositiveIntegerField(default=0, verbose_name='Image height auto field', editable=False),
        ),
        migrations.AddField(
            model_name='newsimage',
            name='size_w',
            field=models.PositiveIntegerField(default=0, verbose_name='Image width auto field', editable=False),
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(height_field=b'size_h', width_field=b'size_w', upload_to=b'news_images'),
        ),
    ]
