# -*- coding: utf-8 -*-
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.test import TestCase

from ..models import Account
from ..emails import token_expired


class TokenExpiredTest(TestCase):

    def test_send_email(self):
        account = Account(manager_email='frantisek@vocilka.xxx')

        token_expired(account)

        self.assertTrue(hasattr(mail, 'outbox'))
        self.failUnlessEqual(len(mail.outbox), 1)
        self.assertIsInstance(mail.outbox[0], EmailMultiAlternatives)
        self.assertEqual(mail.outbox[0].to, [account.manager_email])
