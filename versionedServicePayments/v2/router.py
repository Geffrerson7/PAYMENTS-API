from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'services', api.ServiceUserViewSet, basename='services')
router.register(r'services-crud', api.ServiceAdminViewSet, basename='services-crud')
router.register(r'payments', api.PaymentUserViewSet, basename='payments')
router.register(r'payments-crud', api.PaymentAdminViewSet, basename='payments-crud')
router.register(r'expired', api.PaymentExpiredUserViewSet, basename='expired')
router.register(r'expired-crud', api.PaymentExpiredAdminViewSet, basename='expired-crud')

api_urlpatterns = router.urls