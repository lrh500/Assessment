from django.shortcuts import render
from .models import country_id, Global_tem, Globaltem_change


# Create your views here.
def index(request):
    return render(request, 'climate_change/index.html')


def country_list(request):
    countries = country_id.objects.all()
    headers = ['id', 'Country']
    data = [[country_id.id, country_id.country] for country_id in countries]
    return render(request, 'climate_change/country_list.html', {'headers': headers, 'data': data})


def global_tem_list(request):
    global_tem = Global_tem.objects.all()
    return render(request, 'climate_change/global_tem_list.html', {'global_tem': global_tem})


def global_tem_change_view(request):
    global_tem_changes = Globaltem_change.objects.all()
    return render(request, 'climate_change/global_tem_change.html', {'global_tem_changes': global_tem_changes})


# def country_name(request):


def country_by_name(request, value):
    cities = Global_tem.objects.filter(country=value).exclude(averageTemperature='').exclude(averageTemperature=None)
    city = cities.first()
    if city.latitude.endswith('N'):
        cities_lat = float(city.latitude[:-1])
    else:
        cities_lat = -float(city.latitude[:-1])
    if city.longitude.endswith('E'):
        cities_lng = float(city.longitude[:-1])
    else:
        cities_lng = -float(city.longitude[:-1])
    context = {
        'cities': cities,
        'cities_lat': cities_lat,
        'cities_lng': cities_lng,
    }
    return render(request, 'climate_change/country_by_name.html', context)


def check_by_date(request,date):
    dates=Global_tem.objects.filter(dt=date)
    return render(request,'climate_change/check_by_date.html',{'dates':dates})