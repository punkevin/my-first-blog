# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('NroConv', models.IntegerField(serialize=False, primary_key=True)),
                ('CodCli', models.IntegerField()),
                ('FecPubli', models.DateField()),
                ('FecBuenaPro', models.DateField()),
                ('Nomenclatura', models.CharField(max_length=100)),
                ('FecReinicio', models.DateField()),
                ('CodObjC', models.IntegerField()),
                ('DescObjeto', models.CharField(max_length=1000)),
                ('CodSNIP', models.CharField(max_length=10)),
                ('ValRefer', models.DecimalField(decimal_places=2, max_digits=9)),
                ('RutaDoc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ConvPers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('CodPers', models.IntegerField()),
                ('CodCargo', models.IntegerField()),
                ('Experiencia', models.CharField(max_length=500)),
                ('ExpNroMeses', models.IntegerField()),
                ('ExpNroDias', models.IntegerField()),
                ('CorrProf', models.IntegerField()),
                ('FlgCIPVigen', models.IntegerField()),
                ('NroConv', models.ForeignKey(to='GestionConvocatoria.Convocatoria')),
            ],
        ),
        migrations.CreateModel(
            name='ResulConv',
            fields=[
                ('CorrConv', models.IntegerField(serialize=False, primary_key=True)),
                ('Empresa', models.CharField(max_length=200)),
                ('FlgGana', models.CharField(max_length=1)),
                ('EvalTec', models.DecimalField(decimal_places=2, max_digits=5)),
                ('EvalEcon', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Observac', models.CharField(max_length=2000)),
                ('NroConv', models.ForeignKey(to='GestionConvocatoria.Convocatoria')),
            ],
        ),
    ]
