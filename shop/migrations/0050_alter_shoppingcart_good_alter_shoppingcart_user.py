# Generated by Django 4.2.4 on 2023-09-17 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0049_shoppingcart_cost_shoppingcart_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='good',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.goods'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
