from django.urls import path
from . import views


urlpatterns = [
    path('service-type/', views.ServiceTypeView.as_view(), name='service_type'),
]
