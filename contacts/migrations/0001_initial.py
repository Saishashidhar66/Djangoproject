# Generated by Django 3.0.7 on 2021-03-17 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('car_id', models.IntegerField(null=True)),
                ('customer_need', models.CharField(max_length=100, null=True)),
                ('car_title', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('phone', models.CharField(max_length=20, null=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]