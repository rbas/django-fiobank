# -*- coding: utf-8 -*-
import datetime
import pygal
from pygal.style import Style
from django.db.models import Count, Sum
from django.utils.translation import ugettext as _
from django_fiobank.models import Transaction


def generate_income_issue_graph(account_id, year):
    date = datetime.datetime(year, 1, 1)
    income__transaction_list = Transaction.objects.extra(
        select={'year': 'EXTRACT(year FROM  CAST ("date" as DATE))',
                'month': 'EXTRACT(month from CAST ("date" as DATE))'}).values(
        'year', 'month').annotate(dcount=Count('date'), sum_amount=Sum(
        'amount')) \
        .order_by('year', 'month').filter(amount__gt=0,
                                          date__gte=date, account_id=account_id)

    issue_transaction_list = Transaction.objects.extra(
        select={'year': 'EXTRACT(year FROM  CAST ("date" as DATE))',
                'month': 'EXTRACT(month from CAST ("date" as DATE))'}).values(
        'year', 'month').annotate(dcount=Count('date'), sum_amount=Sum(
        'amount')) \
        .order_by('year', 'month').filter(amount__lt=0,
                                          date__gte=date, account_id=account_id)

    def month_to_str(month):
        return datetime.datetime(year, month, 1).strftime('%B')

    income_custom_list = {int(trans['month']): trans for trans in
                          income__transaction_list}
    issue_custom_list = {int(trans['month']): trans for trans in
                         issue_transaction_list}

    month_labels = []
    income_amount_list = []
    issue_amount_list = []
    for month_number in range(1, 12):
        month_labels.append(month_to_str(month_number))
        if month_number in income_custom_list:
            income_amount_list.append(
                income_custom_list[month_number]['sum_amount'])
        else:
            income_amount_list.append(None)

        if month_number in issue_custom_list:
            issue_amount_list.append(
                issue_custom_list[month_number]['sum_amount'] * -1)
        else:
            issue_amount_list.append(None)

    custom_style = Style(
        foreground='#FFFFFF',
        foreground_light='#fff',
        foreground_dark='#fff',
        opacity='.6',
        opacity_hover='.9',
        transition='400ms ease-in',
        colors=('#36E336', '#F72D05'))

    bar_chart = pygal.Bar(fill=True, interpolate='cubic',
                          style=custom_style)

    bar_chart.x_labels = month_labels
    bar_chart.add(_(u'Income'), income_amount_list)
    bar_chart.add(_(u'Issue'), issue_amount_list)
    return bar_chart.render()