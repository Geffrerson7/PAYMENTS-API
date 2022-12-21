from payments.models import PaymentUser2, ExpiredPayments
from appservices.models import Service
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .pagination import StandardResultsSetPagination
from .serializer import PaymentSerializer, PaymentExpiratedSerializer, ServiceSerializer
from rest_framework.authentication import BasicAuthentication

class PaymentAdminViewSet(viewsets.ModelViewSet):
    """Vista de los pagos para el admin"""
    queryset = PaymentUser2.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes=[IsAdminUser]
    search_fields = ['paymentDate', 'expirationDate']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        crear=super().create(request, *args, **kwargs)
        last=PaymentUser2.objects.order_by("-id").first()
        pago=PaymentUser2.objects.get(id=last.id)
        if pago.paymentDate > pago.expirationDate:
            expired=ExpiredPayments(payment_user=pago,penalty_fee_amount=25)
            expired.save()
        return crear
    
class PaymentUserViewSet(viewsets.ModelViewSet):
    """Vista de los pagos para los usuarios"""
    queryset = PaymentUser2.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes=[IsAuthenticated]
    search_fields = ['paymentDate', 'expirationDate']
    http_method_names=['get','post']
    throttle_scope = 'payments-user'
    authentication_classes=[BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        crear=super().create(request, *args, **kwargs)
        last=PaymentUser2.objects.order_by("-id").first()
        pago=PaymentUser2.objects.get(id=last.id)
        if pago.paymentDate > pago.expirationDate:
            expired=ExpiredPayments(payment_user=pago,penalty_fee_amount=25)
            expired.save()
        return crear

class PaymentExpiredUserViewSet(viewsets.ModelViewSet):
    """Vista de los pagos expirados para los usuarios"""
    queryset = ExpiredPayments.objects.all()
    serializer_class = PaymentExpiratedSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    http_method_names=['get']
    throttle_scope = 'expired-user'
    authentication_classes=[BasicAuthentication]

class PaymentExpiredAdminViewSet(viewsets.ModelViewSet):
    """Vista de los pagos expirados para el admin"""
    queryset = ExpiredPayments.objects.all()
    serializer_class = PaymentExpiratedSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAdminUser]

class ServiceUserViewSet(viewsets.ModelViewSet):
    """Vista de los servicios para los usuarios"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    http_method_names=['get']
    throttle_scope = 'services-user'
    

class ServiceAdminViewSet(viewsets.ModelViewSet):
    """Vista de los servicios para el admin"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAdminUser]
    