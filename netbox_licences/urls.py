from django.urls import path
from . import views
from .utilities.urls import URLPatternGenerator

from .rapidcrud import rapidcrud

urlpatterns = rapidcrud.generate_urls()
