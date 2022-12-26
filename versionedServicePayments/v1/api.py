from payments.models import PaymentUser1
from .serializer import PaymentSerializerv1
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class PaymentViewSet1(viewsets.ModelViewSet):
    """Vista de los pagos para los usuarios"""
    queryset = PaymentUser1.objects.all()
    serializer_class = PaymentSerializerv1
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes=[IsAuthenticated]
    search_fields = ['user', 'paymentDate', 'name_service']
    throttle_scope = 'payment_1'
    http_method_names=['get','post']
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)
