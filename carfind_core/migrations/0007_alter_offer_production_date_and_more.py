# Generated by Django 5.0.6 on 2024-06-04 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carfind_core', '0006_offerimage_offer_alter_offer_production_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='production_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 4, 18, 25, 40, 393752)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 18, 25, 40, 393752)),
        ),
    ]
