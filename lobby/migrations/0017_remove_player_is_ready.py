# Generated by Django 3.1 on 2020-08-25 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0016_player_is_ready'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='is_ready',
        ),
    ]