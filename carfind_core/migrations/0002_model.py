# Generated by Django 5.0.6 on 2024-06-03 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carfind_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carfind_core.make')),
            ],
        ),
    ]
