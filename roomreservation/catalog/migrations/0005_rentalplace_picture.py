# Generated by Django 4.1.7 on 2023-02-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_rentalplace_city_alter_rentalplace_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalplace',
            name='picture',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
