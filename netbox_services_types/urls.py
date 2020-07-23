from django.urls import path
from . import views


urlpatterns = [
    path('services-types-list/', views.ServiceTypeView.as_view(), name='services_types_list'),
]
