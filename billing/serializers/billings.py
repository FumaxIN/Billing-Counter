from rest_framework import serializers

from rest_framework.generics import get_object_or_404
from billing.models import Product, Customer, Bill
from billing.serializers import ProductSerializer, CustomerSerializer, UserSerializer


class BillSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    employee = UserSerializer(read_only=True)
    customer_id = serializers.UUIDField(write_only=True)
    products_id = serializers.ListField(child=serializers.JSONField(), write_only=True)

    class Meta:
        model = Bill
        fields = (
            'external_id',
            'url',
            'amount',
            'orders',
            'customer',
            'employee',
            'customer_id',
            'products_id',
            'created_at',
            'modified_at',
            'deleted'
        )
        read_only_fields = ('external_id', 'url', 'amount', 'orders', 'created_at', 'modified_at', 'deleted')

    def create(self, validated_data):
        customer_external_id = validated_data.pop('customer_id')
        products_extId = validated_data.pop('products_id')
        if len(products_extId) == 0:
            raise serializers.ValidationError('Products list cannot be empty')

        customer = get_object_or_404(Customer, external_id=customer_external_id)
        employee = self.context['request'].user

        validated_data['employee'] = employee
        validated_data['customer'] = customer

        orders = []
        amount = 0

        for product in products_extId:
            product_dict = product

            product_id = list(product_dict.keys())[0]
            product_quantity = list(product_dict.values())[0]

            item = get_object_or_404(Product, external_id=product_id)

            products = {"product": ProductSerializer(item).data, "quantity": product_quantity}
            total = item.price * product_quantity
            products["total"] = str(total)

            orders.append(products)
            amount += total

        validated_data['orders'] = orders
        validated_data['amount'] = str(amount)

        return Bill.objects.create(**validated_data)


