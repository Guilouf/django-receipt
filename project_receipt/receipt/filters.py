from django_filters import FilterSet
from receipt.models import Company


class CompanyFilter(FilterSet):
    class Meta:
        model = Company
        fields = {'name': ['icontains'],
                  'tags': ['exact']}
