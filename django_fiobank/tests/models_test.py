# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase
from ..models import Account, Transaction


class AccountTest(TestCase):

    def test_account_number_full(self):
        account_number = '42424242'
        bank_code = '2100'

        account = Account(account_number=account_number, bank_code=bank_code)
        expected = '{0}/{1}'.format(account_number, bank_code)

        self.assertEqual(expected, account.account_number_full)

    def test_account_number_full_with_empty_data(self):
        account = Account()
        self.assertEqual('', account.account_number_full)

        account = Account(bank_code='021')
        self.assertEqual('/021', account.account_number_full)

        account = Account(account_number='43242-43')
        self.assertEqual('43242-43/', account.account_number_full)


class TransactionTest(TestCase):

    def test_assigin_data(self):
        data = {
            'transaction_id': 23848928329,
            'date': datetime.date.today(),
            'amount': 666.42,
            'currency': 'CZK',
            'account_number': '058740259847485',
            'account_name': 'Tuhiik',
            'bank_code': '0034982039',
            'bic': '0029384324',
            'bank_name': 'Fio bank',
            'constant_symbol': '0045',
            'variable_symbol': '0123456789',
            'specific_symbol': '0987654321',
            'user_identification': 'Frantisek Vocilka',
            'recipient_message': 'Payment of your invoice',
            'type': 'Bank fee',
            'executor': 'Milos Zenam',
            'specification': 'Bank fee',
            'comment': 'Payment of your invoice',
            'instruction_id': '098765432112345',
            'unsupported_field': 'blah'
        }

        transaction = Transaction()
        transaction.assign(data)

        for property_name, value in data.items():
            if hasattr(transaction, property_name):
                self.assertEqual(value, transaction.__getattribute__(
                    property_name))

    def test_account_full(self):
        account_number = '40293842034'
        bank_code = '0021'
        transaction = Transaction(account_number=account_number,
                                  bank_code=bank_code)

        expected = '{0}/{1}'.format(account_number, bank_code)

        self.assertEqual(expected, transaction.account_full)

    def test_account_number_full_with_empty_data(self):
        transaction = Transaction()
        self.assertEqual('', transaction.account_full)

        transaction = Transaction(bank_code='021')
        self.assertEqual('/021', transaction.account_full)

        transaction = Transaction(account_number='43242-43')
        self.assertEqual('43242-43/', transaction.account_full)
