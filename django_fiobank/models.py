# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ('TransactionManager', 'Account', 'Transaction')


class TransactionManager(models.Manager):

    def get_last_transaction(self, account_id):
        data = self.get_query_set().filter(account_id=account_id).order_by(
            '-transaction_id')[:1]
        if data:
            return data[0]
        else:
            return None


class Account(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    account_number = models.CharField(_('Account number'), max_length=16)
    bank_code = models.CharField(_('Bank code'), max_length=10)
    token = models.CharField(_('Token'), max_length=64)
    token_expire = models.DateField(_('Token expire'),
                                    help_text=_('Date of expiration token.'))
    manager_email = models.EmailField(_('Manager email'),
                                      help_text=_('E-mail address bank account'
                                                  ' manager or owner.'))

    @property
    def account_number_full(self):
        if self.account_number or self.bank_code:
            return '{0}/{1}'.format(self.account_number, self.bank_code)
        else:
            return ''

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
        unique_together = ('account_number', 'bank_code')

    def __unicode__(self):
        return self.name


class Transaction(models.Model):
    account = models.ForeignKey(Account, verbose_name=_('Account'))
    transaction_id = models.BigIntegerField(_('Transaction id'))
    date = models.DateField(_('Date'))
    amount = models.FloatField(_('Amount'))
    currency = models.CharField(_('Currency'), max_length=3)
    account_number = models.CharField(_('Account number'), max_length=17)
    account_name = models.CharField(_('Account name'), max_length=255,
                                    blank=True, null=True)
    bank_code = models.CharField(_('Bank code'), max_length=10)
    bic = models.CharField(_('Bic'), max_length=11, blank=True, null=True)
    bank_name = models.CharField(_('Bank name'), max_length=255)
    constant_symbol = models.CharField(_('Constant symbol'), max_length=4,
                                       blank=True, null=True)
    variable_symbol = models.CharField(_('Variable symbol'), max_length=10,
                                       blank=True, null=True)
    specific_symbol = models.CharField(_('Specific symbol'), max_length=10,
                                       blank=True, null=True)
    user_identification = models.CharField(_('User identification'),
                                           max_length=50, blank=True,
                                           null=True)
    recipient_message = models.CharField(_('Recipient message'),
                                         max_length=140, blank=True,
                                         null=True)
    type = models.CharField(_('Type'), max_length=255)
    executor = models.CharField(_('Executor'), max_length=255, blank=True,
                                null=True)
    specification = models.CharField(_('Specification'), max_length=255,
                                     blank=True, null=True)
    comment = models.CharField(_('Comment'), max_length=255, blank=True,
                               null=True)
    instruction_id = models.CharField(_('Instruction id'), max_length=15)

    objects = TransactionManager()

    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
        unique_together = ('instruction_id',)

    def __unicode__(self):
        return u'{0}'.format(self.transaction_id)

    def assign(self, transaction_data):
        ''' Assign data from dict

        :param transaction_data: Transaction data
        :type transaction_data: dict
        '''
        for property_name, value in transaction_data.items():
            if hasattr(self, property_name):
                self.__setattr__(property_name, value)

    @property
    def account_full(self):
        if self.account_number or self.bank_code:
            return '{0}/{1}'.format(self.account_number, self.bank_code)
        else:
            return ''
