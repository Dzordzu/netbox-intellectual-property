from django import forms
from django_rq import get_queue

from .models import SoftwareProvider, Licence, Software

from mptt.forms import TreeNodeChoiceField

from utilities.forms import (
    APISelectMultiple,
    DynamicModelMultipleChoiceField,
    StaticSelect2Multiple,
    BootstrapMixin,
    DatePicker
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

    software = DynamicModelMultipleChoiceField(
        queryset=Software.objects.all(),
        required=False,
        widget=APISelectMultiple(
            api_url="/api/plugins/licences/software/",
        )
    )

    site = DynamicModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False,
    )

    date_valid_after = forms.DateField(
        required=False,
        input_formats='%Y,%m,%d',
        widget=DatePicker()
    )

    date_valid_before = forms.DateField(
        required=False,
        input_formats='%Y,%m,%d',
        widget=DatePicker()
    )


    class Meta:
        model = Licence
        fields = [
            "q",
            "site",
            "software",
        ]

class SoftwareProviderForm(BootstrapMixin, forms.ModelForm):
    name = forms.CharField(
        required=True, label="Short name", help_text="Short name of the software provider"
    )

    full_name = forms.CharField(
        required=True, label="Full name", help_text="Full name of the software provider"
    )

    class Meta:
        model = SoftwareProvider
        fields = [
            "name",
            "full_name"
        ]

