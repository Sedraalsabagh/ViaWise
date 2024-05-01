# Generated by Django 5.0.3 on 2024-05-01 07:27

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0021_flightschedule_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('conditions', models.TextField(blank=True, null=True)),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
            ],
        ),
    ]
