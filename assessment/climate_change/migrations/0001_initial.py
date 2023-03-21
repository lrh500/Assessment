# Generated by Django 4.1.7 on 2023-03-21 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country_id',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Country', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Global_tem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dt', models.TextField()),
                ('AverageTemperature', models.TextField()),
                ('AverageTemperatureUncertainty', models.TextField()),
                ('City', models.TextField()),
                ('Latitude', models.TextField()),
                ('Longitude', models.TextField()),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Global_tem', to='climate_change.country_id')),
            ],
        ),
    ]