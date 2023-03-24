# Generated by Django 4.1.7 on 2023-03-24 15:14

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
                ('id', models.IntegerField()),
                ('country', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Global_tem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.TextField()),
                ('averageTemperature', models.TextField()),
                ('averageTemperatureUncertainty', models.TextField()),
                ('city', models.TextField()),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='global_tem', to='climate_change.country_id')),
            ],
        ),
    ]
