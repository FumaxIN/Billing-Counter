from rest_framework import serializers

from billing.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'external_id',
            'url',
            'name',
            'email',
            'phone',
            'address',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('external_id', 'created_at', 'updated_at')

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
