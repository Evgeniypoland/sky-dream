# Generated by Django 4.2.4 on 2023-09-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_wingsuits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=20)),
                ('description', models.CharField(default='null', max_length=200)),
                ('price', models.CharField(default='null', max_length=10)),
            ],
        ),
    ]
