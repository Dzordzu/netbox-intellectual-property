from django import forms
from django_rq import get_queue

from utilities.forms import BootstrapMixin
from .models import ServiceType


class ServiceTypeFilterForm(BootstrapMixin, forms.ModelForm):

    q = forms.CharField(required=False, label="Search")

    class Meta:
        model = ServiceType
        fields = [
            "q",
        ]

