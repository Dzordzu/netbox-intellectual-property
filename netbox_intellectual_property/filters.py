import django_filters
from django.db.models import Q

from utilities.filters import NameSlugSearchFilterSet


from .models import SoftwareProvider


class SoftwareProviderFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(method="search", label="Search")

    class Meta:
        model = SoftwareProvider
        fields = ["id", "name"]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(id__icontains=value)
            | Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)
