# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_auto_20181122_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='nro_doc',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
