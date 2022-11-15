from django.urls import path
from rest_framework import routers

from apps.agenda.views import AgendaViewSet

router = routers.DefaultRouter()
router.register(r'', AgendaViewSet, basename='agenda')

urlpatterns = router.urls
