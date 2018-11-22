# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20181122_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='nro_documento',
            new_name='numero_docuemnto',
        ),
    ]
