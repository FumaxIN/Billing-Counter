from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce

from billing.models import Product, User
from billing.serializers import ProductSerializer, UserSerializer


class Analytics(APIView):
    def get(self, request):
        top_employee = User.objects.annotate(
            total_revenue=Coalesce(
                Sum('bill__amount', output_field=FloatField()),
                0.0
            )
        ).order_by('-total_revenue').first()

        top_product = Product.objects.all().order_by('-total_units_sold').first()

        return Response(
            {
                'top_employee': {
                    'user': UserSerializer(top_employee).data,
                    'total_revenue': top_employee.total_revenue
                },
                'top_product': {
                    'name': ProductSerializer(top_product).data,
                    'total_units_sold': top_product.total_units_sold
                }
            },
            status=status.HTTP_200_OK
        )
