# Generated by Django 4.2.3 on 2023-08-13 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_expense_day_expense_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='day',
            field=models.CharField(default=datetime.datetime(2023, 8, 13, 14, 51, 47, 779627, tzinfo=datetime.timezone.utc), max_length=100),
        ),
    ]
