from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .filters import (
    SoftwareProviderFilter,
    LicencesFilter
)
from .forms import (
    SoftwareProviderFilterForm,
    LicencesFilterForm,
    SoftwareProviderForm
)
from .models import (
    SoftwareProvider,
    Licence,
)
from .tables import (
    SoftwareProviderTable,
    LicenceTable,
)

from .utilities.views import CRUDViewGenerator

####
## SoftwareProvider
####

software_provider_generator = CRUDViewGenerator("SoftwareProvider")
SoftwareProviderListView = software_provider_generator.list()
SoftwareProviderCreateView = software_provider_generator.create()
SoftwareProviderBulkDeleteView = software_provider_generator.bulk_delete()

class SoftwareProviderEditView(PermissionRequiredMixin, ObjectEditView):
   """ Edit existing Software Provider """
   permission_required = 'netbox_licences.edit_softwareprovider'
   queryset = SoftwareProvider.objects.all()
   model = SoftwareProvider

software_type_generator = CRUDViewGenerator("SoftwareType")
SoftwareTypeListView = software_type_generator.list()
SoftwareTypeCreateView = software_type_generator.create()
SoftwareTypeBulkDeleteView = software_type_generator.bulk_delete()

software_generator = CRUDViewGenerator("Software")
SoftwareListView = software_generator.list()
SoftwareCreateView = software_generator.create()
SoftwareBulkDeleteView = software_generator.bulk_delete()

class LicenceListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'netbox_licences.view_licence'
    queryset = Licence.objects.all()
    filterset = LicencesFilter
    filterset_form = LicencesFilterForm
    table = LicenceTable
    template_name = "netbox_licences/licences_list.html"
