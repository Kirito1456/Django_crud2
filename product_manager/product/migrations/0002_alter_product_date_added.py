# Generated by Django 3.2 on 2023-09-11 18:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 18, 32, 36, 717728, tzinfo=utc)),
        ),
    ]
