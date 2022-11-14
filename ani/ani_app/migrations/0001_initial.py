# Generated by Django 4.1.3 on 2022-11-14 12:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='title')),
                ('count', models.IntegerField(default=0, verbose_name='count')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250, null=True, verbose_name='comment')),
                ('date_published', models.DateTimeField(default=datetime.datetime(2022, 11, 14, 12, 59, 48, 266871, tzinfo=datetime.timezone.utc), null=True, verbose_name='date_published')),
                ('is_published', models.BooleanField(default=False, null=True, verbose_name='is_published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ('date_published',),
            },
        ),
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
                ('date_published', models.DateTimeField(default=datetime.datetime(2022, 11, 14, 12, 59, 48, 268872, tzinfo=datetime.timezone.utc), verbose_name='date published')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('is_published', models.BooleanField(default=False, verbose_name='is published')),
                ('count_comments', models.IntegerField(default=0, verbose_name='count_comments')),
                ('category', models.ManyToManyField(blank=True, null=True, to='ani_app.categories', verbose_name='category')),
                ('pk_comm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ani_app.comments', verbose_name='pk_comm')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
                'db_table': 'anime_serials',
                'ordering': ('date_published', 'genre'),
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='title')),
                ('season', models.IntegerField(null=True, verbose_name='season')),
                ('image', models.ImageField(null=True, upload_to='series_image/', verbose_name='image')),
                ('date_published', models.DateTimeField(default=datetime.datetime(2022, 11, 14, 12, 59, 48, 269871, tzinfo=datetime.timezone.utc), verbose_name='date published')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('is_published', models.BooleanField(default=False, verbose_name='is_published')),
                ('serial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ani_app.serials', verbose_name='serial')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
                'ordering': ('date_published',),
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='serial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ani_app.serials', verbose_name='serial'),
        ),
        migrations.AddField(
            model_name='categories',
            name='serial',
            field=models.ManyToManyField(blank=True, null=True, to='ani_app.serials', verbose_name='serials'),
        ),
    ]
