# Generated by Django 3.0.5 on 2023-12-19 19:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_movie_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='average_rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_src',
            field=models.CharField(max_length=255),
        ),
    ]
