# -*- coding: utf-8 -*-
import datetime
import logging
from requests import HTTPError
import fiobank
from .models import Transaction, Account
from .emails import token_expired

logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.addHandler(logging.StreamHandler())

token_expired_default_sender = token_expired


def download_and_save_bank_transactions():

    today = datetime.date.today()
    account_list = Account.objects.all()
    for account in account_list:

        if account.token_expire < today:
            continue

        try:
            last_transaction = Transaction.objects.get_last_transaction(
                account.id)

            client = fiobank.FioBank(token=account.token)

            if last_transaction:
                lookup_params = {'from_id': last_transaction.transaction_id}
                transaction_list = client.last(**lookup_params)
            else:
                from_date = '{0}-01-01'.format(today.year)
                transaction_list = client.last(from_date=from_date)

        except HTTPError as e:
            logger.error('Error in process account {0}'.format(account))
            logger.exception(e)
            break
        else:
            for data in transaction_list:
                try:
                    bank_trans = Transaction()
                    bank_trans.account = account
                    bank_trans.assign(data)
                    bank_trans.save()
                except Exception:
                    pass


def check_account_token_time_validity(
        email_sender=token_expired_default_sender):
    """ Check token validity and send emails if expired.

    :param email_sender: Function for send notification email. Default si
    token_expired.
    """
    minimal_validation_date = datetime.date.today() + datetime.timedelta(days=7)
    account_list = Account.objects.all()
    for account in account_list:
        if account.token_expire >= minimal_validation_date:
            email_sender(account)
