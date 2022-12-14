# Generated by Django 4.1 on 2022-09-06 22:27

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
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('country', models.CharField(max_length=75)),
                ('state_province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LocationPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locationposts', to='shop_travel_work.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locationposts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocalItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('store', models.CharField(max_length=100)),
                ('store_url', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.CharField(max_length=200)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localitems', to='shop_travel_work.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localitems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocalFare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommend', models.IntegerField(choices=[(-1, 'Stay Away'), (0, 'Neutral'), (1, 'Recommend')])),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('establishment', models.CharField(max_length=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localfares', to='shop_travel_work.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localfares', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
