from django.urls import reverse
from rest_framework.test import APITestCase
from urllib.parse import quote, unquote


class ViewsTestCase(APITestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_weather(self):
        self.client.get(reverse('index')+'?city=Москва')
        self.client.get(reverse('index')+'?city=Казань')
        response = self.client.get(reverse('index')+'?city=Москва')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertTrue('previous_cities' in response.cookies)
        unquoted_cities = [unquote(city) for city in response.cookies['previous_cities'].value.split(',')]
        self.assertTrue('Москва', 'Казань' in unquoted_cities)

    def test_error_city(self):
        self.client.get(reverse('index') + '?city=новосиб')
        response = self.client.get(reverse('index') + '?city=ddd')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertTrue('previous_cities' in response.cookies)
        unquoted_cities = [unquote(city) for city in response.cookies['previous_cities'].value.split(',')]
        self.assertEqual(unquoted_cities, [''])

    def test_cookies_set(self):
        previous_cities = ['Москва', 'Казань']
        self.client.cookies['previous_cities'] = ','.join([quote(city) for city in previous_cities])
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('previous_cities' in response.cookies)
        unquoted_cities = [unquote(city) for city in response.cookies['previous_cities'].value.split(',')]
        self.assertEqual(unquoted_cities, previous_cities)

    def test_cookies_del(self):
        previous_cities = ['Москва', 'Казань']
        self.client.cookies['previous_cities'] = ','.join([quote(city) for city in previous_cities])
        response = self.client.get(reverse('index')+'?clear=true')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('previous_cities' in response.cookies)
        unquoted_cities = [unquote(city) for city in response.cookies['previous_cities'].value.split(',')]
        self.assertEqual(unquoted_cities, [''])

    def test_history(self):
        response = self.client.get(reverse('history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/history.html')

    def test_about_api(self):
        response = self.client.get(reverse('about-api'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about-api.html')

    def test_about_site(self):
        response = self.client.get(reverse('about-site'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about-site.html')
