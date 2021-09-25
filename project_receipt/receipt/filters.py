from django_filters import FilterSet, DateFromToRangeFilter, RangeFilter
from django_filters.widgets import RangeWidget

from receipt.models import Receipt, Establishment, Company


class ReceiptFilter(FilterSet):
    # i am not filtering on datetime, if needed i can use isodatetimefilter
    date_range = DateFromToRangeFilter(field_name='date', widget=RangeWidget(attrs={'type': 'date'}))
    amount_range = RangeFilter(field_name='amount')

    class Meta:
        model = Receipt
        fields = {'tags': ['exact'],
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
