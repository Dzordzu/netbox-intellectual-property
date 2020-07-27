from django import forms
from django_rq import get_queue

from utilities.forms import BootstrapMixin
from .models import SoftwareProvider


class SoftwareProviderFilterForm(BootstrapMixin, forms.ModelForm):

    q = forms.CharField(required=False, label="Search")

    class Meta:
        model = SoftwareProvider
        fields = [
            "q",
        ]

