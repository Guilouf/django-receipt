from django_filters import FilterSet
from receipt.models import Establishment, Company


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
