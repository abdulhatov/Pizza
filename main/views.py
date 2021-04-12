from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pizza
from .serializers import PizzaListSerializer

# Create your views here.

class PizzaListView(APIView):

    def get(self, request):
        pizzas = Pizza.objects.filter()
        serializer = PizzaListSerializer(pizzas, many=True)
        return Response(serializer.data)
