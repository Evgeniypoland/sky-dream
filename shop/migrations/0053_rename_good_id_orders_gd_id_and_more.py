# Generated by Django 4.2.4 on 2023-09-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0052_remove_orders_category_remove_orders_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='good_id',
            new_name='gd_id',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='user_id',
            new_name='us_id',
        ),
        migrations.AlterField(
            model_name='orders',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_order',
            field=models.IntegerField(null=True),
        ),
    ]
