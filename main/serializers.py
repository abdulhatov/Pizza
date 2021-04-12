from  rest_framework import serializers

from .models import Pizza

class PizzaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = ('order', 'name', 'price', 'type')

