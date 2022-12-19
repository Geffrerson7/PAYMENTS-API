from .api import GetAllService, ServiceViewSet
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v2/service-payments/services/crud', ServiceViewSet, 'crud-services')
urlpatterns = [
    
    path('api/v2/service-payments/services/', GetAllService.as_view(),name='getAllService'),
    
]

urlpatterns += router.urls