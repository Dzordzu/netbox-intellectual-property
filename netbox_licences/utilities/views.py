import re
from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView
from pydoc import locate

class CRUDViewGenerator:

    name = ""
    package = "netbox_licences"

    def __init__(self, name):
        self.name = name


    def list(self):
        return type(
            self.name + "ListView",
            (PermissionRequiredMixin, ObjectListView),
            {
                "permission_required": self.package + ".view_" + self.name.lower(),
                "queryset": locate(self.package + ".models." + self.name).objects.all(),
                "filterset": locate(self.package + ".filters." + self.name + "Filter"),
                "filterset_form": locate(self.package + ".forms." + self.name + "FilterForm"),
                "table": locate(self.package + ".tables." + self.name + "Table"),
                "template_name": "netbox_licences/" + re.sub(r'(?<!^)(?=[A-Z])', '_', self.name).lower() + "s_list.html"
            }
        )

