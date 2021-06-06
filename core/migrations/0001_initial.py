# Generated by Django 3.2 on 2021-05-17 19:29

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('maker', models.CharField(max_length=100, verbose_name='Fabricante')),
                ('release_date', models.DateField(max_length=10, verbose_name='Data de lançamento')),
                ('description', models.TextField(max_length=200, verbose_name='Descrição')),
                ('body', models.CharField(max_length=200, verbose_name='Corpo')),
                ('os', models.CharField(max_length=50, verbose_name='Sistema operacional')),
                ('storage', models.CharField(max_length=50, verbose_name='Armazenamento')),
                ('display_size_pixels', models.CharField(max_length=100, verbose_name='Tamanho da tela (pixels)')),
                ('camera_pixels', models.CharField(max_length=50, verbose_name='Resolução da Câmera')),
                ('camera_pixels_unit', models.CharField(max_length=50, verbose_name='Resolução da Câmera (unidade)')),
                ('ram_size', models.CharField(max_length=50, verbose_name='Memória RAM')),
                ('ram_size_unit', models.CharField(max_length=50, verbose_name='Memória RAM (unidade)')),
                ('chipset_short', models.CharField(max_length=50, verbose_name='Processador')),
                ('batery_size', models.CharField(max_length=50, verbose_name='Capacidade da bateria')),
                ('batery_size_unit', models.CharField(max_length=50, verbose_name='Capaciadade da bateria (unidade)')),
                ('batery_type', models.CharField(max_length=50, verbose_name='Tipo de bateria')),
                ('image', stdimage.models.StdImageField(upload_to='smartphone_img', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Smartphone',
                'verbose_name_plural': 'Smartphones',
            },
        ),
    ]