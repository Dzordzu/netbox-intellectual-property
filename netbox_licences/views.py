from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View



from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .filters import SoftwareProviderFilter
from .forms import SoftwareProviderFilterForm
from .models import SoftwareProvider
from .tables import SoftwareProviderTable

class SoftwareProviderListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'netbox_licences.view_softwareprovider'
    queryset = SoftwareProvider.objects.all()
    filterset = SoftwareProviderFilter
    filterset_form = SoftwareProviderFilterForm
    table = SoftwareProviderTable
    template_name = "netbox_licences/software_providers_list.html"
