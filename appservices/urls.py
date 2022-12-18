from .api import GetAllService
from django.urls import path
from rest_framework import routers

#router = routers.DefaultRouter()

urlpatterns = [
    
    path('api/v2/service-payments/services/', GetAllService.as_view(),name='getAllService'),
]

#urlpatterns = router.urls