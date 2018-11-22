# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_member_nro_doc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='numero_docuemnto',
        ),
    ]
