# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    change_form_template = 'django_fiobank/admin/account/change.html'


class AmountFilter(SimpleListFilter):
    title = _('Transaction type')

    parameter_name = 'transaction_type'

    def lookups(self, request, model_admin):
        return (
            ('all', _('All')),
            ('income', _('Income')),
            ('issue', _('Issue')),
        )

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                                                    self.parameter_name: lookup,
                                                    }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() == 'income':
            return queryset.filter(amount__gt=0)
        elif self.value() == 'issue':
            return queryset.filter(amount__lt=0)
        elif self.value() == 'all':
            return queryset


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'transaction_id', 'date', 'account_full', 'amount', 'currency',
        'bank_name', 'constant_symbol', 'variable_symbol',
        'specific_symbol', 'type',
        'executor', 'comment')
    list_filter = ('account__name', AmountFilter,)
    search_fields = ('account_number',)
    date_hierarchy = 'date'


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
