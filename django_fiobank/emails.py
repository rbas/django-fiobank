# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def token_expired(account):
    """
    Send email to bank account manager

    :param account: Instance of Account model.
    :type account: Account
    """
    site = Site.objects.get_current()
    subject = _('Token expired time validity')
    context = {
        'site_domain': site.domain,
        'site_name': site.name,
        'subject': subject,
        'account_name': account.name,
        'account_number_full': account.account_number_full
    }

    html_content = loader.render_to_string(
        'django_fiobank/emails/token_expired.html', context)

    text_content = loader.render_to_string(
        'django_fiobank/emails/token_expired.txt', context)

    to = account.manager_email
    from_email = settings.DEFAULT_FROM_EMAIL

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
