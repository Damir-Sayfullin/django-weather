from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import SearchHistory


class ApiTestCase(APITestCase):
    def test_api_all(self):
        city_1 = SearchHistory.objects.create(city='Москва', search_count=1)
        city_2 = SearchHistory.objects.create(city='Казань', search_count=2)
        city_3 = SearchHistory.objects.create(city='Санкт-Петербург', search_count=3)
        url = reverse('api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        for city in response.data:
            city['last_searched'] = ''
        self.assertEqual(response.data, [
            {'id': 1, 'city': 'Москва', 'search_count': 1, 'last_searched': ''},
            {'id': 2, 'city': 'Казань', 'search_count': 2, 'last_searched': ''},
            {'id': 3, 'city': 'Санкт-Петербург', 'search_count': 3, 'last_searched': ''}])

    def test_api_city(self):
        city_1 = SearchHistory.objects.create(city='Москва', search_count=1)
        city_2 = SearchHistory.objects.create(city='Казань', search_count=2)
        city_3 = SearchHistory.objects.create(city='Санкт-Петербург', search_count=3)
        url = reverse('api') + '?city=Казань'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        for city in response.data:
            city['last_searched'] = ''
        self.assertEqual(response.data, [
            {'id': 2, 'city': 'Казань', 'search_count': 2, 'last_searched': ''}])
