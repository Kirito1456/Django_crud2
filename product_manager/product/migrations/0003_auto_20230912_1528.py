# Generated by Django 3.2 on 2023-09-12 07:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 7, 28, 28, 110829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
