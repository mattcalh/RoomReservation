# Generated by Django 4.1.7 on 2023-02-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_rentalplace_city_alter_rentalplace_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalplace',
            name='city',
            field=models.CharField(help_text='Enter the name of the city where the place is located', max_length=50),
        ),
        migrations.AlterField(
            model_name='rentalplace',
            name='street',
            field=models.CharField(help_text='Enter the name of the street where the place is located', max_length=200),
        ),
    ]
