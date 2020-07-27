from django import forms
from django_rq import get_queue

from utilities.forms import BootstrapMixin
from .models import SoftwareProvider, Licence, Software


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
    software = forms.ModelChoiceField(
        queryset=Software.objects.all(),
        required=False,
        help_text="Licences filter"
    )

    class Meta:
        model = Licence
        fields = [
            "q",
            "inventory_number",
            "software"
        ]
