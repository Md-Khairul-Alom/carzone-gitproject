# Generated by Django 4.2.2 on 2023-06-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_passengers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milleage',
            field=models.IntegerField(),
        ),
    ]
