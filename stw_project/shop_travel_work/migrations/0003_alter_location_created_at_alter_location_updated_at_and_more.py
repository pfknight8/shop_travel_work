# Generated by Django 4.1 on 2022-09-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_travel_work', '0002_localfare_created_at_localfare_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='locationpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='locationpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
