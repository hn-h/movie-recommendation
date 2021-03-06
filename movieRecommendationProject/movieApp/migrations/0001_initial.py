# Generated by Django 3.2.4 on 2021-06-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieID', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('genres', models.CharField(max_length=30)),
                ('image', models.URLField()),
                ('link', models.URLField()),
                ('plot', models.TextField()),
                ('rate', models.FloatField()),
                ('votes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieIDs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movId', models.CharField(max_length=30)),
            ],
        ),
    ]
