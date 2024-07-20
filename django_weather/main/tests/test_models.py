from django.urls import reverse
from rest_framework.test import APITestCase
from ..models import SearchHistory


class ModelsTestCase(APITestCase):
    def test_model_str(self):
        city_1 = SearchHistory.objects.create(city='Москва', search_count=1)
        city_2 = SearchHistory.objects.create(city='Казань', search_count=5)
        city_3 = SearchHistory.objects.create(city='Санкт-Петербург', search_count=10)
        str_1 = 'Москва - 1 - '
        str_2 = 'Казань - 5 - '
        str_3 = 'Санкт-Петербург - 10 - '
        for city in [city_1, city_2, city_3]:
            city.last_searched = ''
        self.assertEqual(str(city_1), str_1)
        self.assertEqual(str(city_2), str_2)
        self.assertEqual(str(city_3), str_3)
