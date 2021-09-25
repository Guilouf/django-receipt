from django.forms import DateTimeInput
from django_filters import FilterSet, IsoDateTimeFilter

from receipt.models import Receipt, Establishment, Company


class ReceiptFilter(FilterSet):
    date_gte = IsoDateTimeFilter(field_name='date', lookup_expr='gte', widget=DateTimeInput(
            attrs={
                'type': 'datetime-local'},
            ))
    date_lte = IsoDateTimeFilter(field_name='date', lookup_expr='lte', widget=DateTimeInput(
        attrs={
            'type': 'datetime-local'},
    ))

    class Meta:
        model = Receipt
        fields = {'amount': ['gte', 'lte'],
                  'tags': ['exact'],
                  'establishment__name': ['icontains'],
                  'establishment__company__name': ['icontains']}


class EstablishmentFilter(FilterSet):
    class Meta:
        model = Establishment
        fields = {'name': ['icontains'],
                  'city': ['icontains']}


class CompanyFilter(FilterSet):
    class Meta:
        model = Company
        fields = {'name': ['icontains'],
                  'tags': ['exact']}
