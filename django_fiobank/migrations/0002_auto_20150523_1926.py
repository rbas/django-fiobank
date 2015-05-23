# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_fiobank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account_number',
            field=models.CharField(verbose_name='Account number', max_length=30),
            preserve_default=True,
        ),
    ]
