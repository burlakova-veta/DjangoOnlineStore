from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True, allow_blank=False)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('id',)


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True, allow_blank=False)

    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('id',)
