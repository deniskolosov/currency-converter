from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView

from fetcher.models import CurrencyRateBaseUSD
from fetcher.serializers import RatesSerializer


class RatesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CurrencyRateBaseUSD.objects.all()
    serializer_class = RatesSerializer


class LatestRate(RetrieveAPIView):
    queryset = CurrencyRateBaseUSD.objects.all()
    serializer_class = RatesSerializer

    def get_object(self, *args, **kwargs):
        return self.queryset.latest('date')


class HomePageView(TemplateView):
    template_name = "home.html"
