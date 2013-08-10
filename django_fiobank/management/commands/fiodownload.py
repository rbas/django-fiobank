# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from ...utils import run


class Command(BaseCommand):
    help = 'Download and save bank transactions.'

    def handle(self, *args, **options):
        run()
