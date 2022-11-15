from django.urls import path
from rest_framework import routers

from apps.conductores.views import ConductorViewSet

router = routers.DefaultRouter()
router.register(r'', ConductorViewSet, basename='conductores')

urlpatterns = router.urls
