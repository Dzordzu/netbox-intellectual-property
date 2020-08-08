from rest_framework.viewsets import ModelViewSet
from netbox_licences.models import *
from .serializers import *
from netbox_licences.filters import *

class SoftwareViewSet(ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    filterset_class = SoftwareFilter

class SoftwareProviderViewSet(ModelViewSet):
    queryset = SoftwareProvider.objects.all()
    serializer_class = SoftwareProviderSerializer
    filterset_class = SoftwareProviderFilter

class SoftwareTypeViewSet(ModelViewSet):
    queryset = SoftwareType.objects.all()
    serializer_class = SoftwareTypeSerializer
    filterset_class = SoftwareTypeFilter

class LicenceViewSet(ModelViewSet):
    queryset = Licence.objects.all()
    serializer_class = LicenceSerializer

