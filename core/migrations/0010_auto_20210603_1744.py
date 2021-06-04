# Generated by Django 3.2 on 2021-06-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210603_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='body_build',
            field=models.CharField(max_length=100, verbose_name='Construção'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='body_weight',
            field=models.CharField(max_length=100, verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='identification_id',
            field=models.CharField(max_length=100, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='main_camera_type',
            field=models.CharField(max_length=100, verbose_name='Tipo de Câmera Principal'),
        ),
    ]
