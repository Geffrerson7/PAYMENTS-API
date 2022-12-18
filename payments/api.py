from .models import Payment_user_1
from rest_framework import viewsets
from rest_framework import filters
from .serializer import PaymentSerializer1
from .pagination import StandardResultsSetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class PaymentViewSet1(viewsets.ModelViewSet):
    queryset = Payment_user_1.objects.all()
    serializer_class = PaymentSerializer1
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes=[IsAuthenticated]
    authentication_classes=[BasicAuthentication]
    search_fields = ['user', 'paymentDate', 'name_service']
    throttle_scope = 'payment_1'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


