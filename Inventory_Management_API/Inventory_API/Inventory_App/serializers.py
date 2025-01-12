from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'description', 'quantity', 'price', 'category', 'date_added', 'last_updated', 'added_by', 'updated_by']
