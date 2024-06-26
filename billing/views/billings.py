from rest_framework import permissions, status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from billing.models import Bill, Product, Customer, User
from billing.serializers import BillSerializer


class BillViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """
    products_id to be provided as:
    [
        {
            "product_id": "external_id",
            "quantity": 1
        },
        {
            "product_id": "external_id",
            "quantity": 2
        }
    ]
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "url"