from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from billing.models import Product, Customer, User, Bill
from billing.serializers import ProductSerializer, CustomerSerializer, UserSerializer


class BillSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    customer = CustomerSerializer(read_only=True)
    employee = UserSerializer(read_only=True)
    customer_id = serializers.UUIDField(write_only=True)
    products_id = serializers.ListField(child=serializers.UUIDField(), write_only=True)

    class Meta:
        model = Bill
        fields = (
            'external_id',
            'url',
            'amount',
            'products',
            'customer',
            'employee',
            'customer_id',
            'products_id',
            'created_at',
            'modified_at',
            'deleted'
        )
        read_only_fields = ('external_id', 'url', 'amount', 'created_at', 'modified_at', 'deleted')

    def create(self, validated_data):
        customer_external_id = validated_data.pop('customer_id')
        products_external_id = validated_data.pop('products_id')
        if len(products_external_id) == 0:
            raise serializers.ValidationError('Products list cannot be empty')

        customer = get_object_or_404(Customer, external_id=customer_external_id)
        employee = self.context['request'].user

        products = Product.objects.filter(external_id__in=products_external_id)
        if len(products) != len(products_external_id):
            raise serializers.ValidationError('Invalid product id')

        validated_data['employee'] = employee
        validated_data['customer'] = customer
        validated_data['amount'] = sum([product.price for product in products])
        bill = Bill.objects.create(**validated_data)
        bill.products.add(*products)

        return bill
