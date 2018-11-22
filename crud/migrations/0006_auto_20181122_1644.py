# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20181122_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='numero_docuemnto',
            field=models.CharField(max_length=40),
        ),
    ]
