from decimal import Decimal
from unittest import TestCase
from unittest.mock import patch, Mock

from requests import HTTPError

from fetcher.models import CurrencyRateBaseUSD
from fetcher.tasks import fetch_currency_rates


class TestCreateRateRecord(TestCase):
    @patch('fetcher.tasks.requests.get')
    def test_get_rates(self, requests_patch):
        requests_patch.return_value = Mock(
            json=Mock(return_value={
                'disclaimer': 'Usage subject to terms: https://openexchangerates.org/terms',
                'license': 'https://openexchangerates.org/license',
                'timestamp': 1575212363,
                'base': 'USD',
                'rates': {'CZK': 23.1762, 'EUR': 0.907593, 'PLN': 3.91715, 'USD': 1}}))
        fetch_currency_rates()
        last_rate = CurrencyRateBaseUSD.objects.last()
        self.assertEqual(last_rate.czk, Decimal('23.1762'))
        self.assertEqual(last_rate.pln, Decimal('3.91715'))
        self.assertEqual(last_rate.eur, Decimal('0.90759'))

    @patch('fetcher.tasks.requests')
    def test_get_rates_raises_HTTPError(self, requests_patch):

        requests_patch.get.side_effect = HTTPError
        with self.assertRaises(HTTPError):
            fetch_currency_rates()
