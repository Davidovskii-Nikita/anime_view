# Generated by Django 4.1.2 on 2022-10-28 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ani_app', '0013_alter_comments_options_alter_comments_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 19, 36, 1, 210197, tzinfo=datetime.timezone.utc), verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='serials',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 19, 36, 1, 211197, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AlterModelTable(
            name='comments',
            table=None,
        ),
    ]
