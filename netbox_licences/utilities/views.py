import re
from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView
from pydoc import locate

class CRUDViewGenerator:
    """
        Generator for view classes
        Simple metaclass usage in order to create basic CRUD views.
        Automatically changes names cases, styles etc.

    """

    name = ""
    package = "netbox_licences"

    def __init__(self, name):
        self.name = name

    def __camel_to_snake_name(self):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', self.name).lower()

    def __insert_space_name(self):
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', self.name)

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
                "template_name": "netbox_licences/common_list.html",
                "extra_context": lambda self, name=self.__insert_space_name() : {"title_text" : name}
            }
        )

    def create(self):
        return type(
            self.name + "CreateView",
            (PermissionRequiredMixin, ObjectEditView),
            {
                "permission_required": self.package + ".add_" + self.name.lower(),
                "model": locate(self.package + ".models." + self.name),
                "queryset": locate(self.package + ".models." + self.name).objects.all(),
                "model_form": locate(self.package + ".forms." + self.name + "Form"),
                "template_name": "netbox_licences/common_edit.html",
                "table": locate(self.package + ".tables." + self.name + "Table"),
                "default_return_url": "plugins:netbox_licences:" + self.__camel_to_snake_name() + "s_list",
            }
        )

    def bulk_delete(self):
        return type(
            self.name + "BulkDeleteView",
            (PermissionRequiredMixin, BulkDeleteView),
            {
                "permission_required": self.package + ".delete_" + self.name.lower(),
                "queryset": locate(self.package + ".models." + self.name).objects.all(),
                "filterset": locate(self.package + ".filters." + self.name + "Filter"),
                "table": locate(self.package + ".tables." + self.name + "Table"),
                "default_return_url": "plugins:netbox_licences:" + self.__camel_to_snake_name() + "s_list"
            }
        )

