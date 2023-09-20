# Generated by Django 4.2.4 on 2023-09-19 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0069_alter_defects_email_alter_goods_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='image',
            field=models.ImageField(upload_to='sales'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.goods'),
        ),
    ]
