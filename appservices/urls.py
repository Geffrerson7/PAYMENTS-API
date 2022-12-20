from .api import ServiceUserViewSet, ServiceAdminViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'services', ServiceUserViewSet, basename='services-user')
router.register(r'services-crud', ServiceAdminViewSet, basename='crud-services')
urlpatterns = [
    path('api/v2/service-payments/', include(router.urls)),
]