# Generated by Django 3.2 on 2021-06-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210603_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='display_type_technology',
            field=models.CharField(default='', max_length=100, verbose_name='Tecnologia da Tela'),
            preserve_default=False,
        ),
    ]
