# Generated by Django 4.2.4 on 2023-09-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_customers_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
    ]
