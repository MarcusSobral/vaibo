# Generated by Django 3.2.4 on 2021-06-17 02:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_produtos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='client_score',
            field=models.CharField(max_length=10, null=True, verbose_name='Cliente_score'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='expert_score',
            field=models.CharField(max_length=10, null=True, verbose_name='Expert_score'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='id',
            field=models.CharField(default=uuid.UUID('9d49aa1b-b08a-43f0-bd04-366c47f837d9'), max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
