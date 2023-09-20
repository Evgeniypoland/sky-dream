# Generated by Django 4.2.4 on 2023-09-18 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0067_alter_orders_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='currency',
            field=models.CharField(choices=[('€', 'Euro'), ('$', 'Dollars')], default='$', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.goods'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='good_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.orders'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='user_name',
            field=models.CharField(max_length=20),
        ),
    ]
