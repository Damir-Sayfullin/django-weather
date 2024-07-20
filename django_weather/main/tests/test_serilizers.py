from rest_framework.test import APITestCase
from ..models import SearchHistory
from ..serializers import SearchHistorySerializer


class SerializersTestCase(APITestCase):
    def test_serializer(self):
        city_1 = SearchHistory.objects.create(city='Москва', search_count=1)
        city_2 = SearchHistory.objects.create(city='Казань', search_count=2)
        city_3 = SearchHistory.objects.create(city='Санкт-Петербург', search_count=3)
        serializer_data = SearchHistorySerializer([city_1, city_2, city_3], many=True).data
        for city in serializer_data:
            city['last_searched'] = ''
        self.assertEqual(serializer_data, [
            {'id': 1, 'city': 'Москва', 'search_count': 1, 'last_searched': ''},
            {'id': 2, 'city': 'Казань', 'search_count': 2, 'last_searched': ''},
            {'id': 3, 'city': 'Санкт-Петербург', 'search_count': 3, 'last_searched': ''}])
