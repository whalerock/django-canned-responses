# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canned_responses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cannedresponse',
            name='response_headers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='cannedresponse',
            name='request_method',
            field=models.CharField(db_index=True, max_length=32, choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'PATCH', b'PATCH')]),
        ),
    ]
