# Generated by Django 5.1.1 on 2024-10-12 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_entities_rpgstats_remove_player_health_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='owner',
        ),
        migrations.AddField(
            model_name='entities',
            name='equipment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.equipment'),
            preserve_default=False,
        ),
    ]
