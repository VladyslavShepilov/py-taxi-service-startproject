# Generated by Django 4.2.4 on 2024-01-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_alter_car_options_alter_driver_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]