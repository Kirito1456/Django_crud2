# Generated by Django 3.2 on 2023-09-11 13:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_added', models.DateField(default=datetime.datetime(2023, 9, 11, 13, 45, 19, 357290, tzinfo=utc))),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Books', 'Books')], max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
    ]
