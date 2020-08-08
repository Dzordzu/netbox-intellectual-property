from django.urls import path
from . import views
from .utilities.urls import URLPatternGenerator

_urlpatterns_generators = [
    URLPatternGenerator("SoftwareProvider"),
    URLPatternGenerator("SoftwareType"),
]

urlpatterns = [
    path('licences/', views.LicenceListView.as_view(), name='licences_list'),
]

for gen in _urlpatterns_generators:
    urlpatterns.append(gen.list())
    urlpatterns.append(gen.add())
    urlpatterns.append(gen.bulkDelete())
