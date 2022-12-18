from django.urls import path
from rest_framework import routers
from .api import PaymentViewSet1

router = routers.DefaultRouter()

router.register('', PaymentViewSet1, 'payment1')

urlpatterns = router.urls