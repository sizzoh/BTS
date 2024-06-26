# Generated by Django 4.2.3 on 2023-08-20 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_expense_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='day',
            field=models.CharField(default=datetime.datetime(2023, 8, 20, 7, 24, 22, 171176, tzinfo=datetime.timezone.utc), max_length=100),
        ),
    ]
