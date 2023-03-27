from django.urls import path
from . import views

urlpatterns = [
    path('country_list', views.country_list, name='country_list'),
    path('', views.index, name='index'),
    path('global_tem_list/', views.global_tem_list, name='global_tem_list'),
    path('global_tem_changes/', views.global_tem_change_view, name='global_tem_changes'),
    path('country_by_name/<str:value>/', views.country_by_name, name='country_by_name'),
    path('check_by_date/<str:date>/',views.check_by_date, name='check_by_date'),
]