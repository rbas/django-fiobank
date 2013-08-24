# -*- coding: utf-8 -*-
import datetime
import unittest
from django.test import TestCase

mock_library_imported = False
try:
    from mock import patch
except ImportError:
    mock_library_imported = True

from ..models import Account, Transaction
from ..utils import check_account_token_time_validity,\
    download_and_save_bank_transactions


def _create_accounts():
    today = datetime.date.today()
    thirty_days_interval = datetime.timedelta(days=30)
    Account.objects.create(name='Tuhiik', account_number='3232',
                           bank_code='0021', token='f32#22',
                           token_expire=today + thirty_days_interval)

    Account.objects.create(name='My fio account', account_number='2323',
                           bank_code='2100', token='fsaretq2',
                           token_expire=today - thirty_days_interval)


def _destroy_accounts():
    Account.objects.all().delete()


class CheckTokenTimeValidityTest(TestCase):

    @classmethod
    def tearDownClass(cls):
        super(CheckTokenTimeValidityTest, cls).tearDownClass()
        _destroy_accounts()

    def test_send_email(self):
        _create_accounts()
        today = datetime.date.today()

        def fake_token_expired(account):
            if account.token_expire < today:
                self.assertGreater(today, account.token_expire)

        check_account_token_time_validity(email_sender=fake_token_expired)


class FioBankMock(object):

    def __init__(self, *args, **kwargs):
        super(FioBankMock, self).__init__()

    def last(self, from_id=None, from_date=None):
        return [{
                'comment': u'N\xe1kup:  \u010d\xe1stka 2769.00 CZK',
                'recipient_message': u'N\xe1kup:  \u010d\xe1stka 2769.00 CZK',
                'user_identifiaction': u'N\xe1kup:  \u010d\xe1stka 2769.00 CZK',
                'currency': 'CZK', 'amount': -2769.0,
                'instruction_id': '42424', 'executor': u'František Vocílka',
                'date': datetime.date.today(), 'type': u'Platba kartou',
                'transaction_id': '234242'}]


class DownloadAndSaveTransactionsTest(TestCase):

    @classmethod
    def tearDownClass(cls):
        super(DownloadAndSaveTransactionsTest, cls).tearDownClass()
        _destroy_accounts()

    @unittest.skipIf(mock_library_imported, 'Required mock library')
    @patch('fiobank.FioBank', FioBankMock)
    def test_run(self):
        _create_accounts()

        download_and_save_bank_transactions()

        transaction_list = Transaction.objects.all()
        self.assertEqual(1, len(transaction_list))
