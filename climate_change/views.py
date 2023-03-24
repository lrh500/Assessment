from django.shortcuts import render
from .models import country_id


# Create your views here.
def country_list(request):
    countries = country_id.objects.all()
    headers = ['id', 'Country']
    data = [[country_id.id, country_id.country] for country in countries]
    return render(request, 'country_list.html', {'headers': headers, 'data': data})
