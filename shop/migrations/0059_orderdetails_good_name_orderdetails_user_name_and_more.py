# Generated by Django 4.2.4 on 2023-09-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0058_rename_total_order_orderdetails_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='good_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='user_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='good_name',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
