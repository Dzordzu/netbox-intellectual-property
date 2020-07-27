import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn

from .models import SoftwareProvider

class SoftwareProviderTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = SoftwareProvider
        fields = (
            "name",
        )
