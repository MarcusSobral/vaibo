# Generated by Django 3.2 on 2021-06-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210603_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='identification_announced_date',
            field=models.DateField(verbose_name='Data de Anúncio'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='identification_released_date',
            field=models.DateField(verbose_name='Data de Lançamento'),
        ),
    ]
