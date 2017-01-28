# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_draft_add_month_date_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=website.models.get_event_pdf_path)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Event')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
        migrations.AlterField(
            model_name='quote',
            name='attachment',
            field=models.FileField(blank=True, default=None, upload_to=website.models.get_quotes_files_path),
        ),

    ]
