from rest_framework.serializers import ModelSerializer
from netbox_licences.models import Licence, Software

class SoftwareSerializer(ModelSerializer):
    class Meta:
        model = Software
        fields = ('id', 'name', 'provider', 'software_type')


class LicenceSerializer(ModelSerializer):
    class Meta:
        model = Licence
        fields = ('id', 'inventory_number', 'licence_type', 'date_created', 'date_valid', 'amount', 'software', 'tenant')
