# Generated by Django 3.2.9 on 2022-01-14 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('callsign', models.CharField(max_length=8)),
                ('time_position', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('baro_altitude', models.FloatField()),
                ('on_ground', models.BooleanField()),
                ('velocity', models.FloatField()),
                ('true_track', models.FloatField()),
                ('vertical_rate', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
