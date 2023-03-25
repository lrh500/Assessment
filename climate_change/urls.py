from django.urls import path
from . import views


urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('global_tem_list/', views.global_tem_list, name='global_tem_list'),
]