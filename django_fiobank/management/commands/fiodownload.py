# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from ...utils import download_and_save_bank_transactions


class Command(BaseCommand):
    help = 'Download and save bank transactions.'

    def handle(self, *args, **options):
        download_and_save_bank_transactions()
