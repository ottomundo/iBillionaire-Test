from rest_framework import routers, serializers, viewsets
from .models import Company, Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('ticker', 'price', 'change', 'change_perc', 'market_cap', 'volume', 'last_update')
