# Generated by Django 4.2 on 2024-08-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='logo',
            field=models.ImageField(default=None, upload_to='events/logos/', verbose_name='Event Logo'),
        ),
    ]