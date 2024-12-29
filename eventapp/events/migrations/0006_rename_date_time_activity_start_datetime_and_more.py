# Generated by Django 4.2 on 2024-08-14 01:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='date_time',
            new_name='start_datetime',
        ),
        migrations.AddField(
            model_name='activity',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 14, 1, 30, 24, 649290, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='logo',
            field=models.ImageField(upload_to='events/logos/', verbose_name='Event Logo'),
        ),
    ]
