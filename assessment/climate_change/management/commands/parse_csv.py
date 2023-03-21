import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from climate_change.models import country_id

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        country_id.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/assessment/database/countryandid.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                country = country_id.objects.create(
                    id=int(row[0]),
                    Country=row[1],
                )
                country.save()

        print("data parsed successfully")
