from django.shortcuts import render
from .models import country_id, Global_tem, Globaltem_change
import plotly.graph_objs as go
from plotly.offline import plot


# Create your views here.
def index(request):
    return render(request, 'climate_change/index.html')


def country_list(request):
    countries = country_id.objects.all()
    return render(request, 'climate_change/country_list.html', {'countries':countries})


def global_tem_list(request):
    global_tem = Global_tem.objects.all()
    return render(request, 'climate_change/global_tem_list.html', {'global_tem': global_tem})


def global_tem_change_view(request):
    global_tem_changes = Globaltem_change.objects.all()
    return render(request, 'climate_change/global_tem_change.html', {'global_tem_changes': global_tem_changes})


# def country_name(request):


def country_by_name(request, value):
    cities_noorder = Global_tem.objects.filter(country=value).exclude(averageTemperature='').exclude(averageTemperature=None)
    cities = cities_noorder.order_by('averageTemperature')  
    city = cities.first()
    if city.latitude.endswith('N'):
        cities_lat = float(city.latitude[:-1])
    else:
        cities_lat = -float(city.latitude[:-1])
    if city.longitude.endswith('E'):
        cities_lng = float(city.longitude[:-1])
    else:
        cities_lng = -float(city.longitude[:-1])

    x_data = [city.dt for city in cities]
    y_data = [float(city.averageTemperature) for city in cities] 
    trace = go.Scatter(x=x_data, y=y_data, mode='markers')
    data = [trace]
    layout = go.Layout(title='Average Temperature by Date in ' + value, xaxis=dict(title='Date'), yaxis=dict(title='Average Temperature'))
    fig = go.Figure(data=data, layout=layout)
    div = fig.to_html(full_html=False)
    context = {
        'cities': cities,
        'cities_lat': cities_lat,
        'cities_lng': cities_lng,
        'plot_div': div,
        'cities_noorder':cities_noorder,
    }
    return render(request, 'climate_change/country_by_name.html', context)


def check_by_date(request, date):
    datesnoorder = Global_tem.objects.filter(dt=date).exclude(averageTemperature='').exclude(averageTemperature=None)
    dates = datesnoorder.order_by('averageTemperature')
    x_data = [date.country.country for date in dates]
    y_data = [float(date.averageTemperature) for date in dates]
    trace = go.Scatter(x=x_data, y=y_data, mode='markers')
    data = [trace]
    layout = go.Layout(title='Average Temperature by Country in ' + date, xaxis=dict(title='Country'), yaxis=dict(title='Average Temperature'))
    fig = go.Figure(data=data, layout=layout)
    div = fig.to_html(full_html=False)
    context = {
        'dates': dates,
        'plot_div': div,
    }
    return render(request,'climate_change/check_by_date.html',context)




