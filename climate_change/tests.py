from django.test import TestCase
from climate_change.models import country_id, Global_tem, Globaltem_change

class TestCSVData(TestCase):

    def setUp(self):
        # create country data
        country_id.objects.create(id=1, country="Denmark")
        country_id.objects.create(id=2, country="Turkey")
        country_id.objects.create(id=3, country="Kazakhstan")

        # create global temperature data
        denmark = country_id.objects.get(country="Denmark")
        turkey= country_id.objects.get(country="Turkey")
        Global_tem.objects.create(id=1, country=denmark, dt="1828-01-01", averageTemperature="6.068", averageTemperatureUncertainty="1.737", city="Aarhus", latitude="57.05N", longitude="10.33E")
        Global_tem.objects.create(id=6, country=denmark, dt="1828-06-01", averageTemperature="5.788", averageTemperatureUncertainty="3.624", city="Aarhus", latitude="57.05N", longitude="10.33E")
        Global_tem.objects.create(id=7, country=denmark, dt="1828-07-01", averageTemperature="10.644", averageTemperatureUncertainty="1.283", city="Aarhus", latitude="57.05N", longitude="10.33E")

        # create global temperature change data
        Globaltem_change.objects.create(dt="1750-01-01", landAverageTemperature="3.034", landAverageTemperatureUncertainty="3.574", landMaxTemperature="8.242", landMaxTemperatureUncertainty="1.738", landMinTemperature="-3.206", landMinTemperatureUncertainty="2.822", landAndOceanAverageTemperature="12.833", landAndOceanAverageTemperatureUncertainty="0.367")

    def test_country_data_loaded(self):
        """Test that country data is loaded correctly"""
        self.assertEqual(country_id.objects.count(), 3)

    def test_global_tem_data_loaded(self):
        """Test that global temperature data is loaded correctly"""
        self.assertEqual(Global_tem.objects.count(), 3)

    def test_global_tem_change_data_loaded(self):
        """Test that global temperature change data is loaded correctly"""
        self.assertEqual(Globaltem_change.objects.count(), 1)
