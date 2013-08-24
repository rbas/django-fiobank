# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from ...utils import check_account_token_time_validity


class Command(BaseCommand):
    help = 'Checking token time validity and sand email if expired.'

    def handle(self, *args, **options):
        check_account_token_time_validity()
