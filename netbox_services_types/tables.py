import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn

from .models import ServiceType

class ServiceTypeTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = ServiceType
        fields = (
            "name",
        )
