import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn

from .models import SoftwareProvider, Licence, SoftwareType

class SoftwareProviderTable(BaseTable):
    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        model = SoftwareProvider
        fields = (
            "pk",
            "name",
            "full_name"
        )

class SoftwareTypeTable(BaseTable):
    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        model = SoftwareType
        fields = (
            "pk",
            "name",
        )

class LicenceTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = Licence
        fields = (
            "inventory_number",
            "licence_type",
            "date_created",
            "date_valid",
            "amount",
            "software",
            "tenant",
            "site"
        )
