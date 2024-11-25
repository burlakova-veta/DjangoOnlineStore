from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True, allow_blank=False)

    class Meta:
        model = Product
        exclude = ('image', 'full_text',)
        read_only_fields = ('id',)
