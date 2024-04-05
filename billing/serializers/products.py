from rest_framework import serializers
from billing.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'external_id',
            'url',
            'name',
            'description',
            'price',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('external_id', 'created_at', 'updated_at')

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
