# Generated by Django 4.2.4 on 2023-09-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_shoppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='currency',
            field=models.CharField(default='$', max_length=1),
        ),
    ]
