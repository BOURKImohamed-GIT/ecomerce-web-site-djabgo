# Generated by Django 3.1.4 on 2020-12-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0002_auto_20201224_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='marked_price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.PositiveIntegerField(),
        ),
    ]