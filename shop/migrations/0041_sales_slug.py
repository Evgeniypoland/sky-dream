# Generated by Django 4.2.4 on 2023-09-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_alter_sales_new_price_alter_sales_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
