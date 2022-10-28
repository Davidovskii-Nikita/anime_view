# Generated by Django 4.1.2 on 2022-10-28 14:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ani_app', '0009_alter_comments_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 14, 41, 52, 833031, tzinfo=datetime.timezone.utc), verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='serials',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 14, 41, 52, 834031, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='serials',
            name='pk_comm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ani_app.comments', verbose_name='pk_comm'),
        ),
    ]
