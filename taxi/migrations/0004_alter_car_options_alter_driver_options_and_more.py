# Generated by Django 4.2.4 on 2024-01-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0003_alter_driver_license_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('model',), 'verbose_name': 'car', 'verbose_name_plural': 'cars'},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': 'manufacturer', 'verbose_name_plural': 'manufacturers'},
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]