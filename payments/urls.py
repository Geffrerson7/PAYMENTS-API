from django.urls import path, include
from rest_framework import routers
from .api import PaymentViewSet1, PaymentUserViewSet,PaymentAdminViewSet ,PaymentExpiredUserViewSet, PaymentExpiredAdminViewSet

router = routers.DefaultRouter()

router.register(r'v1/payments', PaymentViewSet1, basename='payments-crud-1')
router.register(r'v2/service-payments/payments', PaymentUserViewSet, basename='payments-user')
router.register(r'v2/service-payments/payments-crud', PaymentAdminViewSet, basename='payments-crud')
router.register(r'v2/service-payments/expired', PaymentExpiredUserViewSet, basename='expired-user')
router.register(r'v2/service-payments/expired-crud', PaymentExpiredAdminViewSet, basename='expired')

urlpatterns = [
    path('api/', include(router.urls)),
]