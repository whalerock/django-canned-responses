# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CannedResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('request_method', models.CharField(db_index=True, max_length=32, choices=[(b'GET', b'get'), (b'POST', b'post'), (b'PATCH', b'patch')])),
                ('request_path', models.CharField(max_length=1024, db_index=True)),
                ('response_status_code', models.IntegerField(default=200)),
                ('response_sleep_time', models.IntegerField(default=0)),
                ('response_content_type', models.CharField(max_length=64, choices=[(b'application/json', b'JSON'), (b'text/html', b'HTML')])),
                ('response_payload', models.TextField()),
            ],
            options={
                'verbose_name': 'Canned Response',
                'verbose_name_plural': 'Canned Responses',
            },
        ),
    ]
