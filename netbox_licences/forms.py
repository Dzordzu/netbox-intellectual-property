from django import forms
from django_rq import get_queue

from .models import (
    SoftwareProvider,
    Licence,
    Software,
    SoftwareType,
)
from mptt.forms import TreeNodeChoiceField

from utilities.forms import (
    APISelectMultiple,
    APISelect,
    DynamicModelMultipleChoiceField,
    DynamicModelChoiceField,
    StaticSelect2Multiple,
    BootstrapMixin,
    DatePicker
)

from dcim.models import Site


class SoftwareProviderFilterForm(BootstrapMixin, forms.ModelForm):

    q = forms.CharField(required=False, label="Search")

    class Meta:
        model = SoftwareProvider
        fields = [
            "q",
        ]

class SoftwareTypeFilterForm(BootstrapMixin, forms.ModelForm):

    q = forms.CharField(required=False, label="Search")

    class Meta:
        model = SoftwareType
        fields = [
            "q",
        ]

class SoftwareFilterForm(BootstrapMixin, forms.ModelForm):

    q = forms.CharField(required=False, label="Search")

    software_type = DynamicModelMultipleChoiceField(
        queryset=SoftwareType.objects.all(),
        required=False,
        widget=APISelectMultiple(
            api_url="/api/plugins/licences/software-types/",
        )
    )

    provider = DynamicModelMultipleChoiceField(
        queryset=SoftwareProvider.objects.all(),
        required=False,
        widget=APISelectMultiple(
            api_url="/api/plugins/licences/software-providers/",
        )
    )

    class Meta:
        model = Software
        fields = [
            "q",
            "software_type",
            "provider"
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


class SoftwareTypeForm(BootstrapMixin, forms.ModelForm):

    name = forms.CharField(
        required=True, label="Name", help_text="Name of the software type"
    )


    class Meta:
        model = SoftwareType
        fields = [
            "name",
        ]



class SoftwareForm(BootstrapMixin, forms.ModelForm):

    name = forms.CharField(
        required=True, label="Name", help_text="Name of the software"
    )

    software_type = DynamicModelChoiceField(
        queryset=SoftwareType.objects.all(),
        required=True,
        widget=APISelect(
            api_url="/api/plugins/licences/software-types/",
        )
    )

    provider = DynamicModelChoiceField(
        queryset=SoftwareProvider.objects.all(),
        required=True,
        widget=APISelect(
            api_url="/api/plugins/licences/software-providers/",
        )
    )


    class Meta:
        model = Software
        fields = [
            "name", "provider", "software_type"
        ]
