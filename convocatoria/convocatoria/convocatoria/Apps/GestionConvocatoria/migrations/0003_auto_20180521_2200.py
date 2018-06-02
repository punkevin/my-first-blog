# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionConvocatoria', '0002_auto_20180521_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convpers',
            name='NroConv',
            field=models.ForeignKey(to='GestionConvocatoria.Convocatoria', db_column='NroConv'),
        ),
    ]
