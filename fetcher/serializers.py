from rest_framework import serializers

from fetcher.models import CurrencyRateBaseUSD


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRateBaseUSD
        fields = ['id', 'czk', 'pln', 'eur', 'date']


