from requests import HTTPError

from currency_converter.celery import app
import requests

from fetcher.models import CurrencyRateBaseUSD


@app.task(bind=True)
def fetch_currency_rates(self):
    response = requests.get('https://openexchangerates.org/api/latest.json',
                            params={'app_id': 'c91bdf36ce7e404cbbb3f8ebe37aa8f9', 'symbols': 'CZK,PLN,EUR,USD'})
    try:
        response.raise_for_status()
        response_json = response.json()
    except HTTPError as e:
        raise self.retry(countdown=600, max_retries=5, exc=e)
    except Exception:
        raise
    CurrencyRateBaseUSD.objects.create(
        czk=response_json['rates']['CZK'],
        pln=response_json['rates']['PLN'],
        eur=response_json['rates']['EUR'],
    )
