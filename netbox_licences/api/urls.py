from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('software', SoftwareViewSet)
router.register('software-types', SoftwareTypeViewSet)
router.register('software-providers', SoftwareProviderViewSet)
# router.register('licences', LicenceViewSet)


urlpatterns = router.urls
