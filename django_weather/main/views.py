from django.shortcuts import render
from .models import SearchHistory

# Create your views here.


def index(request):
    context = {}
    if 'city' in request.GET:
        city = request.GET['city']
        # response = requests.get(
        #     f'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m')
        # data = response.json()
        # context['weather_data'] = data
        if True:
            context['status'] = 'ok'
            context['weather_data'] = {'city': city, 'temperature': 20.0}
            search_entry, _ = SearchHistory.objects.get_or_create(city=city)
            search_entry.search_count += 1
            search_entry.save()
        else:
            context['status'] = 'error'
            context['weather_data'] = {'city': city}
    return render(request, 'main/index.html', context)

def history(request):
    history = SearchHistory.objects.order_by('-last_searched')
    return render(request, 'main/history.html', {'history': history})