from rest_framework.serializers import ModelSerializer
from netbox_licences.models import Licence, Software, SoftwareType, SoftwareProvider

class SoftwareProviderSerializer(ModelSerializer):
    class Meta:
        model = SoftwareProvider
        fields = ('id', 'name', "full_name")

class SoftwareTypeSerializer(ModelSerializer):
    class Meta:
        model = SoftwareType
        fields = ('id', 'name')

class SoftwareSerializer(ModelSerializer):
    class Meta:
        model = Software
        fields = ('id', 'name', 'provider', 'software_type')


class LicenceSerializer(ModelSerializer):
    class Meta:
        model = Licence
        fields = ('id', 'inventory_number', 'licence_type', 'date_created', 'date_valid', 'amount', 'software', 'tenant')
