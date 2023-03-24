import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from climate_change.models import country_id,Global_tem

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        country_id.objects.all().delete()
        Global_tem.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/climate_change/database/countryandid.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                country = country_id.objects.create(
                    id=int(row[0]),
                    country=row[1],
                )
                country.save()

            #else:
                #next(reader)

        
        # Global_tem.objects.all().delete()
        # print("table dropped successfully")

        with open(str(base_dir) + '/climate_change/database/GlobalLandTemperaturesByCity.csv', newline='') as f:        
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)   

                
                if row[5] is not '' :
                    con= country_id.objects.filter(country=row[5]).first()
                    global_tem = Global_tem.objects.create(
                        id = int(row[0]),
                        country = con,
                        dt=row[1],
                        averageTemperature=row[2],
                        averageTemperatureUncertainty=row[3],
                        city=row[4],
                        #country_id = countryname,
                        latitude=row[6],
                        longitude=row[7],
                        )

                    # Save the Global_tem object to the database
                    global_tem.save()
            
                else:
                    next(reader)



            print("data parsed successfully")
