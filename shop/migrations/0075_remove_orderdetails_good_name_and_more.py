# Generated by Django 4.2.4 on 2023-09-19 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0074_alter_defects_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='good_name',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='good_name',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user_name',
        ),
    ]
