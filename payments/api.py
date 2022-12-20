from .models import PaymentUser1, PaymentUser2, ExpiredPayments
from rest_framework import viewsets
from rest_framework import filters
from .serializer import PaymentSerializer1, PaymentSerializer, PaymentExpiratedSerializer
from .pagination import StandardResultsSetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.settings import api_settings
from rest_framework.request import Request

class PaymentViewSet1(viewsets.ModelViewSet):
    queryset = PaymentUser1.objects.all()
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

class PaymentUserViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[BasicAuthentication]
    pagination_class = StandardResultsSetPagination
    throttle_scope = 'payments'
    serializer_class = PaymentSerializer

    def get(self, request):
        payments = PaymentUser2.objects.all()
        serializer = PaymentSerializer(payments, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        payments = PaymentSerializer(data=request.data)
         
        if payments.is_valid():
            payments.save()
            #payments.get_value()
            
            return Response(status=status.HTTP_201_CREATED)
        return Response(payments.errors, status=status.HTTP_400_BAD_REQUEST)
       

class PaymentAdminViewSet(viewsets.ModelViewSet):
    queryset = PaymentUser2.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes=[IsAuthenticated]
    authentication_classes=[BasicAuthentication]
    search_fields = ['paymentDate', 'expirationDate']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    #def create(self, request, *args, **kwargs):
        # payment_data=request.data
        # new_payment=PaymentUser2.objects.create()
        # new_payment.save()
        # if new_payment.get_paymentDate() > new_payment.get_expirationDate():
        #     expired_payment=ExpiredPayments.objects.create(payment_user=new_payment.get_user())
        #     expired_payment.save()
        # serializer=PaymentSerializerAdmin(new_payment)

        # return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = PaymentSerializer(data=request.data, many = True)
        else:
            serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class PaymentExpiratedViewSet(viewsets.ModelViewSet):
    queryset = ExpiredPayments.objects.all()
    serializer_class = PaymentExpiratedSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[BasicAuthentication]
        
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)