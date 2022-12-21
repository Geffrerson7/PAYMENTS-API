from django.urls import path, include
from rest_framework import routers
from .api import PaymentViewSet1, PaymentUserViewSet,PaymentAdminViewSet ,PaymentExpiredUserViewSet, PaymentExpiredAdminViewSet

router = routers.DefaultRouter()

router.register(r'payments', PaymentViewSet1, basename='payments-crud-1')
router.register(r'service-payments/payments', PaymentUserViewSet, basename='payments-user')
router.register(r'service-payments/payments-crud', PaymentAdminViewSet, basename='payments-crud')
router.register(r'service-payments/expired', PaymentExpiredUserViewSet, basename='expired-user')
router.register(r'service-payments/expired-crud', PaymentExpiredAdminViewSet, basename='expired')

urlpatterns = [
    path('api/', include(router.urls)),
]