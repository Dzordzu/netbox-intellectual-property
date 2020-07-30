from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .filters import (
    CommonLicencesFilter,
    LicencesFilter
)
from .forms import (
    CommonLicencesFilterForm,
    LicencesFilterForm,
    SoftwareProviderForm
)
from .models import (
    SoftwareProvider,
    Licence
)
from .tables import (
    SoftwareProviderTable,
    LicenceTable
)

class SoftwareProviderListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'netbox_licences.view_softwareprovider'
    queryset = SoftwareProvider.objects.all()
    filterset = CommonLicencesFilter
    filterset_form = CommonLicencesFilterForm
    table = SoftwareProviderTable
    template_name = "netbox_licences/software_providers_list.html"

class SoftwareProviderCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'netbox_licences.add_softwareprovider'
    model=SoftwareProvider
    queryset = SoftwareProvider.objects.all()
    model_form = SoftwareProviderForm
    template_name = "netbox_licences/software_providers_edit.html"
    default_return_url = "plugins:netbox_licences:software_providers_list"


class LicenceListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'netbox_licences.view_licence'
    queryset = Licence.objects.all()
    filterset = LicencesFilter
    filterset_form = LicencesFilterForm
    table = LicenceTable
    template_name = "netbox_licences/licences_list.html"
