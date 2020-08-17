import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn

from .models import SoftwareProvider, Licence, SoftwareType

SOFTWARE_PROVIDER_ACTIONS = """
{% if perms.plugins.change_software_provider %}
    <a href="{% url 'plugins:netbox_licences:software_providers_edit' pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

class SoftwareProviderTable(BaseTable):
    pk = ToggleColumn()

    name = tables.LinkColumn()

    actions = tables.TemplateColumn(
        template_code=SOFTWARE_PROVIDER_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = SoftwareProvider
        fields = (
            "pk",
            "name",
            "full_name",
            "actions"
        )

class SoftwareTypeTable(BaseTable):
    pk = ToggleColumn()

    name = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = SoftwareType
        fields = (
            "pk",
            "name",
        )

class SoftwareTable(BaseTable):
    pk = ToggleColumn()

    name = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = SoftwareType
        fields = (
            "pk",
            "name",
            "software_type",
            "provider"
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
