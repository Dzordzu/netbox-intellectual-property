from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .filters import ServiceTypeFilter
from .forms import ServiceTypeFilterForm
from .models import ServiceType
from .tables import ServiceTypeTable

class ServiceTypeListView(PermissionRequiredMixin, ObjectListView):
    permission_required = "ipam.view_service"
    queryset = ServiceType.objects.all()
    filterset = ServiceTypeFilter
    filterset_form = ServiceTypeFilterForm
    table = ServiceTypeTable
    template_name = "netbox_services_types/services_types_list.html"

