from django.shortcuts import render
from .models import country_id, Global_tem


# Create your views here.
def country_list(request):
    countries = country_id.objects.all()
    headers = ['id', 'Country']
    data = [[country_id.id, country_id.country] for country_id in countries]
    return render(request, 'climate_change/country_list.html', {'headers': headers, 'data': data})

def global_tem_list(request):
    global_tem = Global_tem.objects.all()
    return render(request, 'climate_change/global_tem_list.html', {'global_tem': global_tem})
