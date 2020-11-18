from .models import *
from rest_framework import serializers


class PizzeriasSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(source='distance.km', max_digits=10, decimal_places=2,
                                        required=False, read_only=True)

    class Meta:
        model = Pizzerias
        fields = ('id', 'name', 'city', 'street', 'house_number', 'coordinates', 'distance')