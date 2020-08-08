from rest_framework.viewsets import ModelViewSet
from netbox_licences.models import *
from .serializers import *
from netbox_licences.filters import *
from netbox_licences.utilities.views import CRUDViewGenerator

SoftwareViewSet = CRUDViewGenerator("Software").view_set()
SoftwareProviderViewSet = CRUDViewGenerator("SoftwareProvider").view_set()
SoftwareTypeViewSet = CRUDViewGenerator("SoftwareType").view_set()

class LicenceViewSet(ModelViewSet):
    queryset = Licence.objects.all()
    serializer_class = LicenceSerializer

