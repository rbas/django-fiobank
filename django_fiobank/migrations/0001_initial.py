# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'django_fiobank_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('account_number', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('bank_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'django_fiobank', ['Account'])

        # Adding unique constraint on 'Account', fields ['account_number', 'bank_code']
        db.create_unique(u'django_fiobank_account', ['account_number', 'bank_code'])

        # Adding model 'Transaction'
        db.create_table(u'django_fiobank_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_fiobank.Account'])),
            ('transaction_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('account_number', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('account_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bank_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('bic', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('bank_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('constant_symbol', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('variable_symbol', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('specific_symbol', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('user_identification', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('recipient_message', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('executor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('specification', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('instruction_id', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'django_fiobank', ['Transaction'])

        # Adding unique constraint on 'Transaction', fields ['instruction_id']
        db.create_unique(u'django_fiobank_transaction', ['instruction_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Transaction', fields ['instruction_id']
        db.delete_unique(u'django_fiobank_transaction', ['instruction_id'])

        # Removing unique constraint on 'Account', fields ['account_number', 'bank_code']
        db.delete_unique(u'django_fiobank_account', ['account_number', 'bank_code'])

        # Deleting model 'Account'
        db.delete_table(u'django_fiobank_account')

        # Deleting model 'Transaction'
        db.delete_table(u'django_fiobank_transaction')


    models = {
        u'django_fiobank.account': {
            'Meta': {'unique_together': "(('account_number', 'bank_code'),)", 'object_name': 'Account'},
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'bank_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'django_fiobank.transaction': {
            'Meta': {'unique_together': "(('instruction_id',),)", 'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_fiobank.Account']"}),
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'bank_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'bank_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bic': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'constant_symbol': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'executor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction_id': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'recipient_message': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'specific_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'specification': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_identification': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'variable_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_fiobank']