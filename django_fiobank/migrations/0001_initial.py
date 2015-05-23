# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('account_number', models.CharField(verbose_name='Account number', max_length=16)),
                ('bank_code', models.CharField(verbose_name='Bank code', max_length=10)),
                ('token', models.CharField(verbose_name='Token', max_length=64)),
                ('token_expire', models.DateField(verbose_name='Token expire', help_text='Date of expiration token.')),
                ('manager_email', models.EmailField(verbose_name='Manager email', max_length=75, help_text='E-mail address bank account manager or owner.')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('transaction_id', models.BigIntegerField(verbose_name='Transaction id')),
                ('date', models.DateField(verbose_name='Date')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('currency', models.CharField(verbose_name='Currency', max_length=3)),
                ('account_number', models.CharField(verbose_name='Account number', max_length=17)),
                ('account_name', models.CharField(blank=True, null=True, max_length=255, verbose_name='Account name')),
                ('bank_code', models.CharField(verbose_name='Bank code', max_length=10)),
                ('bic', models.CharField(blank=True, null=True, max_length=11, verbose_name='Bic')),
                ('bank_name', models.CharField(verbose_name='Bank name', max_length=255)),
                ('constant_symbol', models.CharField(blank=True, null=True, max_length=4, verbose_name='Constant symbol')),
                ('variable_symbol', models.CharField(blank=True, null=True, max_length=10, verbose_name='Variable symbol')),
                ('specific_symbol', models.CharField(blank=True, null=True, max_length=10, verbose_name='Specific symbol')),
                ('user_identification', models.CharField(blank=True, null=True, max_length=50, verbose_name='User identification')),
                ('recipient_message', models.CharField(blank=True, null=True, max_length=140, verbose_name='Recipient message')),
                ('type', models.CharField(verbose_name='Type', max_length=255)),
                ('executor', models.CharField(blank=True, null=True, max_length=255, verbose_name='Executor')),
                ('specification', models.CharField(blank=True, null=True, max_length=255, verbose_name='Specification')),
                ('comment', models.CharField(blank=True, null=True, max_length=255, verbose_name='Comment')),
                ('instruction_id', models.CharField(verbose_name='Instruction id', max_length=15)),
                ('account', models.ForeignKey(verbose_name='Account', to='django_fiobank.Account')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together=set([('instruction_id',)]),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('account_number', 'bank_code')]),
        ),
    ]
