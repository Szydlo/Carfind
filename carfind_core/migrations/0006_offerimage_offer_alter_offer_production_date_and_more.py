# Generated by Django 5.0.6 on 2024-06-04 16:24

import carfind_core.models
import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carfind_core', '0005_offerimage_alter_offer_production_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerimage',
            name='offer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='carfind_core.offer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='production_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 4, 18, 24, 46, 407090)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 18, 24, 46, 407090)),
        ),
        migrations.AlterField(
            model_name='offerimage',
            name='image',
            field=models.ImageField(upload_to=carfind_core.models.upload_location),
        ),
    ]