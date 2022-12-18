from django.urls import path
from rest_framework import routers
from .api import PaymentViewSet1

router = routers.DefaultRouter()

router.register('api/v1/service-payments/payments', PaymentViewSet1, 'payment-crud-1')

urlpatterns = router.urls