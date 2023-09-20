# Generated by Django 4.2.4 on 2023-09-10 14:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_customers_delivery_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.customers')),
            ],
        ),
    ]
