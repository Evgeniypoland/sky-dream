# Generated by Django 4.2.4 on 2023-09-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_accessories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Containers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=20)),
                ('description', models.CharField(default='null', max_length=200)),
                ('price', models.CharField(default='null', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Helmets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=20)),
                ('description', models.CharField(default='null', max_length=200)),
                ('price', models.CharField(default='null', max_length=10)),
            ],
        ),
    ]
