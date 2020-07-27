import django_filters
from django.db.models import Q

from utilities.filters import NameSlugSearchFilterSet
from .models import SoftwareProvider, Software, Licence


class CommonLicencesFilter(NameSlugSearchFilterSet):
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

class LicencesFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(method="search", label="Search")

    inventory_number = django_filters.CharFilter(method="search_in_only", label="Inventory Name (only)")

    software = django_filters.ModelMultipleChoiceFilter(
        queryset = Software.objects.all(),
        field_name = "software",
        label = "Software"
    )

    class Meta:
        most = Licence
        fields = [
            "id",
            "inventory_number",
            "date_created",
            "date_valid",
            "amount",
            "software",
            "site",
            "tenant"
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(id__icontains=value)
            | Q(inventory_number__icontains=value)
            | Q(software_number__icontains=value)
            | Q(site__icontains=value)
            | Q(tenant__icontains=value)
        )
        return queryset.filter(qs_filter)

    def search_in_only(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(inventory_number__icontains=value)
        )
        return queryset.filter(qs_filter)
