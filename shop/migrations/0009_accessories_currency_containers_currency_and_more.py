# Generated by Django 4.2.4 on 2023-09-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_parachutes_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='currency',
            field=models.CharField(choices=[('€', 'Euro'), ('$', 'Dollars')], default='$', max_length=1),
        ),
        migrations.AddField(
            model_name='containers',
            name='currency',
            field=models.CharField(choices=[('€', 'Euro'), ('$', 'Dollars')], default='$', max_length=1),
        ),
        migrations.AddField(
            model_name='helmets',
            name='currency',
            field=models.CharField(choices=[('€', 'Euro'), ('$', 'Dollars')], default='$', max_length=1),
        ),
        migrations.AddField(
            model_name='wingsuits',
            name='currency',
            field=models.CharField(choices=[('€', 'Euro'), ('$', 'Dollars')], default='$', max_length=1),
        ),
    ]
