from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')

    class Meta:
        model = Car
        fields = ['id', 'model', 'brand', 'price', 'is_bought', 'buyer', 'buy_time']
