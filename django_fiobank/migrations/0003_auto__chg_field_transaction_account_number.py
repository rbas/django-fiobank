# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Transaction.account_number'
        db.alter_column(u'django_fiobank_transaction', 'account_number', self.gf('django.db.models.fields.CharField')(max_length=17))

    def backwards(self, orm):

        # Changing field 'Transaction.account_number'
        db.alter_column(u'django_fiobank_transaction', 'account_number', self.gf('django.db.models.fields.CharField')(max_length=16))

    models = {
        u'django_fiobank.account': {
            'Meta': {'unique_together': "(('account_number', 'bank_code'),)", 'object_name': 'Account'},
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'bank_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'token_expire': ('django.db.models.fields.DateField', [], {})
        },
        u'django_fiobank.transaction': {
            'Meta': {'unique_together': "(('instruction_id',),)", 'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_fiobank.Account']"}),
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
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