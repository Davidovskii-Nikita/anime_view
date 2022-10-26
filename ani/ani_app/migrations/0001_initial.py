# Generated by Django 4.1.2 on 2022-10-25 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('subtitle', models.CharField(max_length=60, verbose_name=' subtitle')),
                ('type', models.CharField(max_length=20, verbose_name='type')),
                ('studio', models.CharField(max_length=20, verbose_name='studio')),
                ('date_aried', models.DateTimeField(verbose_name='date_aried')),
                ('status', models.CharField(max_length=20, verbose_name='status')),
                ('genre', models.CharField(max_length=30, verbose_name='genre')),
                ('rating', models.CharField(max_length=30, verbose_name='rating')),
                ('duration', models.CharField(max_length=30, verbose_name='duration')),
                ('quality', models.CharField(max_length=30, verbose_name='quality')),
                ('views', models.IntegerField(verbose_name='views')),
                ('image', models.ImageField(upload_to='serials_image/', verbose_name='image')),
                ('text_description', models.TextField(verbose_name='text_description')),
                ('date_published', models.DateTimeField(default=datetime.datetime(2022, 10, 25, 16, 55, 51, 84216, tzinfo=datetime.timezone.utc), verbose_name='date published')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('is_published', models.BooleanField(default=False, verbose_name='is published')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
                'db_table': 'anime_serials',
                'ordering': ('date_published', 'genre'),
            },
        ),
    ]
