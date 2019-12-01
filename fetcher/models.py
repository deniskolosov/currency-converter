from django.db import models


class CurrencyRateBaseUSD(models.Model):
    czk = models.DecimalField(decimal_places=5, max_digits=10)
    pln = models.DecimalField(decimal_places=5, max_digits=10)
    eur = models.DecimalField(decimal_places=5, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Rates for {}".format(self.date)
