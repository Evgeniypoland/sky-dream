# Generated by Django 4.2.4 on 2023-09-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0060_alter_orders_delivery_address_alter_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(null=True),
        ),
    ]
