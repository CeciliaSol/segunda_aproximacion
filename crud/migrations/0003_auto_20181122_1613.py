# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20181116_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='DNI',
            new_name='dni',
        ),
    ]
