import django_filters.rest_framework
from rest_framework.filters import SearchFilter
from django.shortcuts import render, get_object_or_404
from .models import Company, Stock
from rest_framework import viewsets
from .serializers import StockSerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('ticker__ticker',)
    def retrieve(self, request, pk):
        queryset = Stock.objects.all()
        stock = get_object_or_404(queryset, pk=pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)
