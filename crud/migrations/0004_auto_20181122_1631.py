# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20181122_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='dni',
            new_name='nro_documento',
        ),
    ]
