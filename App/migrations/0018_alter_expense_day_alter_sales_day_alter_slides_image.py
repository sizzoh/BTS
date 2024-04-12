# Generated by Django 4.2.3 on 2023-08-31 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_alter_expense_day_alter_expense_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='day',
            field=models.CharField(default=datetime.datetime(2023, 8, 31, 15, 47, 18, 745350, tzinfo=datetime.timezone.utc), max_length=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='day',
            field=models.CharField(default=datetime.datetime(2023, 8, 31, 15, 47, 18, 747344, tzinfo=datetime.timezone.utc), max_length=80),
        ),
        migrations.AlterField(
            model_name='slides',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]