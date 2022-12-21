from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'payments', api.PaymentViewSet1, basename='payments')

api_urlpatterns = router.urls