# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170130_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_es',
            field=wagtail.wagtailcore.fields.StreamField([('body', wagtail.wagtailcore.blocks.StructBlock([('body', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon='pick'))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
