# -*- coding: utf-8 -*-
import datetime
from django import template
from django.utils.safestring import mark_safe
from django_fiobank.graph import generate_income_issue_graph
from django_fiobank.models import Account

register = template.Library()


@register.simple_tag(takes_context=True)
def render_account_graph(context):
    if 'original' in context and isinstance(context['original'], Account):
        year = datetime.date.today().year
        return mark_safe(generate_income_issue_graph(context['object_id'],
                                                     year))
    else:
        return ''
