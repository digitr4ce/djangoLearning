# Generated by Django 5.1.1 on 2024-10-05 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.IntegerField(default=0)),
                ('hunger', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.player')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.inventory')),
                ('resource_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.resourcetypes')),
            ],
        ),
    ]
