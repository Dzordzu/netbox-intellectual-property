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

####
## SoftwareProvider
####

class SoftwareProviderListView(PermissionRequiredMixin, ObjectListView):
    """ List Software Providers """
    permission_required = 'netbox_licences.view_softwareprovider'
    queryset = SoftwareProvider.objects.all()
    filterset = CommonLicencesFilter
    filterset_form = CommonLicencesFilterForm
    table = SoftwareProviderTable
    template_name = "netbox_licences/software_providers_list.html"


class SoftwareProviderCreateView(PermissionRequiredMixin, ObjectEditView):
    """ Create a new Software Provider """
    permission_required = 'netbox_licences.add_softwareprovider'
    model=SoftwareProvider
    queryset = SoftwareProvider.objects.all()
    model_form = SoftwareProviderForm
    template_name = "netbox_licences/software_providers_edit.html"
    default_return_url = "plugins:netbox_licences:software_providers_list"


class SoftwareProviderBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """ Remove multiple Software Providers """
    permission_required = 'netbox_licences.delete_softwareprovider'
    queryset = SoftwareProvider.objects.all()
    filterset = CommonLicencesFilter
    table = SoftwareProviderTable
    default_return_url = "plugins:netbox_licences:software_providers_list"





class LicenceListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'netbox_licences.view_licence'
    queryset = Licence.objects.all()
    filterset = LicencesFilter
    filterset_form = LicencesFilterForm
    table = LicenceTable
    template_name = "netbox_licences/licences_list.html"
