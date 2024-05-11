# Generated by Django 5.0.4 on 2024-05-05 00:01

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generate_unique_code, max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]