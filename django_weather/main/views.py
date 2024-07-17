from django.shortcuts import render
from .models import SearchHistory
import requests
import json

# Create your views here.
weather_codes = {
    0: "Ясно",
    1: "В основном ясно",
    2: "Переменная облачность",
    3: "Пасмурно",
    45: "Туман",
    48: "Осаждающийся изморозь",
    51: "Морось: слабая интенсивность",
    53: "Морось: умеренная интенсивность",
    55: "Морось: сильная интенсивность",
    56: "Замерзающая морось: слабая интенсивность",
    57: "Замерзающая морось: сильная интенсивность",
    61: "Дождь: слабый",
    63: "Дождь: умеренный",
    65: "Дождь: сильный",
    66: "Замерзающий дождь: слабый",
    67: "Замерзающий дождь: сильный",
    71: "Снегопад: слабый",
    73: "Снегопад: умеренный",
    75: "Снегопад: сильный",
    77: "Снежные зерна",
    80: "Ливни: слабые",
    81: "Ливни: умеренные",
    82: "Ливни: сильные",
    85: "Снеговые ливни: слабые",
    86: "Снеговые ливни: сильные",
    95: "Гроза: слабая или умеренная",
    96: "Гроза с градом: слабая",
    99: "Гроза с градом: сильная",
}


def index(request):
    context = {}
    if 'city' in request.GET:
        input_city = request.GET['city']
        context['status'] = 'ok'

        with open('../secret.json') as secret_file:
            key = json.load(secret_file)["DADATA_KEY"]
        url = f"http://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": f"Token {key}"}
        city_response = requests.post(url, json={'query': input_city, 'count': 1}, headers=headers)
        city_data = city_response.json()

        if city_response.status_code == 200 and city_data['suggestions']:
            full_address = str(city_data['suggestions'][0]['unrestricted_value'])
            city = str(city_data['suggestions'][0]['data']['settlement'] or city_data['suggestions'][0]['data']['city'])
            lat, lon = str(city_data['suggestions'][0]['data']['geo_lat']), str(city_data['suggestions'][0]['data']['geo_lon'])

            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"
            weather_response = requests.get(url)
            weather_data = weather_response.json()

            if weather_response.status_code == 200:
                temperature = str(weather_data['current']['temperature_2m'])
                weather_code = str(weather_data['current']['weather_code'])
                weather_description = weather_codes[int(weather_code)]
            else:
                context['status'] = 'weather_error'
        else:
            context['status'] = 'city_not_found'

        if context['status'] == 'ok':
            context['weather_data'] = {
                'input_city': input_city,
                'city': city,
                'full_address': full_address,
                'lat': lat,
                'lon': lon,
                'temperature': temperature,
                'weather_code': weather_code,
                'weather_description': weather_description
            }
            search_entry, _ = SearchHistory.objects.get_or_create(city=city)
            search_entry.search_count += 1
            search_entry.save()
        else:
            context['weather_data'] = {'input_city': input_city}
    return render(request, 'main/index.html', context)

def history(request):
    history = SearchHistory.objects.order_by('-last_searched')
    return render(request, 'main/history.html', {'history': history})