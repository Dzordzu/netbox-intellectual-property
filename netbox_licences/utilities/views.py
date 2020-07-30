import re
from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

class CRUDGenerator:

    name = ""

    def __init__(self, name):
        self.name = name


    def list_view():
        return type(
            name + "ListView",
            (PermissionRequiredMixin, ObjectListView),
            {
                "permission_required": 'netbox_licences.view_' + name.lower(),
                "queryset": type(name, (), {}).objects.all(),
                "filterset": type(name + "Filter", (), {}),
                "filterset_form": type(name + "FilterForm", (), {}),
                "table": type(name + "Table", (), {}),
                "template_name": "netbox_licences/" + re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower() + "_list.html"
            }

        )
