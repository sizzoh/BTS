# Generated by Django 5.0.4 on 2024-04-11 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_alter_expense_day_alter_sales_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='day',
            field=models.CharField(default=datetime.datetime(2024, 4, 11, 5, 50, 24, 363191, tzinfo=datetime.timezone.utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='day',
            field=models.CharField(default=datetime.datetime(2024, 4, 11, 5, 50, 24, 363191, tzinfo=datetime.timezone.utc), max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
