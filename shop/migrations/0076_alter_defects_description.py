# Generated by Django 4.2.4 on 2023-09-19 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0075_remove_orderdetails_good_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defects',
            name='description',
            field=models.TextField(),
        ),
    ]
