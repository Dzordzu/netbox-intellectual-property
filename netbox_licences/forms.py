from django import forms
from django_rq import get_queue

from .models import SoftwareProvider, Licence, Software

from mptt.forms import TreeNodeChoiceField

from utilities.forms import (
    APISelectMultiple,
    DynamicModelMultipleChoiceField,
    StaticSelect2Multiple,
    BootstrapMixin
)

from dcim.models import Site


class CommonLicencesFilterForm(BootstrapMixin, forms.ModelForm):

    q = forms.CharField(required=False, label="Search")

    class Meta:
        model = SoftwareProvider
        fields = [
            "q",
        ]

class LicencesFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(required=False, label="Search")

    inventory_number = forms.CharField(required=False, label="Inventory Number")

    software = DynamicModelMultipleChoiceField(
        queryset=Software.objects.all(),
        required=False,
        to_field_name="id",
        widget=APISelectMultiple(
            api_url="/api/plugins/licences/software/",
        )
    )

    site = DynamicModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False,
        to_field_name="slug",
         widget=APISelectMultiple(
            value_field="slug",
            filter_for={
                'device_id': 'site',
            }
        )
    )

    class Meta:
        model = Licence
        fields = [
            "q",
            "inventory_number",
            "site",
            "software"
        ]
