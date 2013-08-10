==============
Django fiobank
==============

Django-app for managing and processing Fio Bank transaction.

Installation
------------

1. Get and install the code::

    git clone git@github.com:rbas/django-fiobank.git
    cd django-fiobank
    python setup.py install

or install via pip::

    pip install django_fiobank

2. Add 'django_fiobank' to INSTALLED_APPS
3. Run django migration::

    ./manage.py migrate django_fiobank


Usage
-----
Run django in your browser and register Accounts and token for `Fio Bank Api  <http://www.fio.cz/bank-services/internetbanking-api>`_.

Downloading a save your bank transaction::

    ./manage.py fiodownload


Use django.post_save signal on model Transaction for couple your invoice.


For further information read code.


License: ICS
------------
© 2013 Martin Voldrich <rbas.cz@gmail.com>

This work is licensed under `ISC license <https://en.wikipedia.org/wiki/ISC_license>`_.