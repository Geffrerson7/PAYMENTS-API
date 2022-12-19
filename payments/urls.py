from django.urls import path
from rest_framework import routers
from .api import PaymentViewSet1, PaymentAdminViewSet, PaymentUserViewSet, PaymentExpiratedViewSet

router = routers.DefaultRouter()

router.register('api/v1/service-payments/payments', PaymentViewSet1, 'payment-crud-1')
router.register('api/v2/service-payments/payments/crud', PaymentAdminViewSet, 'payment-crud')
router.register('api/v2/service-payments/expirated/crud', PaymentExpiratedViewSet, 'expirated')

urlpatterns = [
    
    path('api/v2/service-payments/payments/', PaymentUserViewSet.as_view(),name='getAllPayments'),
    
]
urlpatterns += router.urls