# Generated by Django 4.1.2 on 2022-10-28 19:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ani_app', '0011_remove_comments_serial_alter_comments_date_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='serial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ani_app.serials', verbose_name='serial'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 19, 29, 31, 606996, tzinfo=datetime.timezone.utc), verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='serials',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 19, 29, 31, 607996, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
