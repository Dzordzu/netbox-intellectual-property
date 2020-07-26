from django.contrib import admin
from .models import SoftwareProvider

@admin.register(SoftwareProvider)
class SoftwareProviderAdmin(admin.ModelAdmin):
    list_display = ('name',)
