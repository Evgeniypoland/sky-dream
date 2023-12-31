# Generated by Django 4.2.4 on 2023-09-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0061_orders_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='user_name',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
