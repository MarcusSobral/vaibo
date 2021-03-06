# Generated by Django 3.2 on 2021-06-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_delete_produtos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('identification_id', models.CharField(max_length=256, verbose_name='ID')),
                ('identification_title', models.CharField(max_length=256, null=True, verbose_name='Título')),
                ('identification_name_maker', models.CharField(max_length=256, verbose_name='Fabricante')),
                ('identification_name', models.CharField(max_length=256, verbose_name='Nome')),
                ('identification_versions', models.CharField(max_length=256, null=True, verbose_name='Versões')),
                ('identification_announced', models.CharField(max_length=256, null=True, verbose_name='Anunciado')),
                ('identification_announced_date', models.DateField(max_length=10, null=True, verbose_name='Data de Anúncio')),
                ('identification_released', models.CharField(max_length=256, null=True, verbose_name='Lançado')),
                ('identification_released_date', models.DateField(max_length=10, null=True, verbose_name='Data de Lançamento')),
                ('identification_status', models.CharField(max_length=256, null=True, verbose_name='Status')),
                ('network_technology', models.CharField(max_length=256, null=True, verbose_name='Tecnologia')),
                ('network_bands_2g', models.CharField(max_length=256, null=True, verbose_name='Bandas 2G')),
                ('network_bands_3g', models.CharField(max_length=256, null=True, verbose_name='Bandas 3G')),
                ('network_bands_4g', models.CharField(max_length=256, null=True, verbose_name='Bandas 4G')),
                ('network_bands_5g', models.CharField(max_length=256, null=True, verbose_name='Bandas 5G')),
                ('body_dimensions', models.CharField(max_length=256, null=True, verbose_name='Dimenções')),
                ('body_weight', models.CharField(max_length=256, null=True, verbose_name='Peso')),
                ('body_build', models.CharField(max_length=256, null=True, verbose_name='Construção')),
                ('body_sim', models.CharField(max_length=256, null=True, verbose_name='SIM')),
                ('body_other', models.CharField(max_length=256, null=True, verbose_name='Corpo Outro(s)')),
                ('display_type', models.CharField(max_length=256, null=True, verbose_name='Tipo de Tela')),
                ('display_size', models.CharField(max_length=256, null=True, verbose_name='Tamanho da Tela')),
                ('display_resolution', models.CharField(max_length=256, null=True, verbose_name='Resolução da Tela')),
                ('display_protection', models.CharField(max_length=256, null=True, verbose_name='Proteção da Tela')),
                ('display_type_technology', models.CharField(max_length=256, null=True, verbose_name='Tecnologia da Tela')),
                ('display_other', models.CharField(max_length=256, null=True, verbose_name='Tela Outro(s)')),
                ('platform_os', models.CharField(max_length=256, null=True, verbose_name='Sistema Operacional')),
                ('platform_chipset', models.CharField(max_length=256, null=True, verbose_name='Processador')),
                ('platform_cpu', models.CharField(max_length=256, null=True, verbose_name='CPU')),
                ('platform_gpu', models.CharField(max_length=256, null=True, verbose_name='GPU')),
                ('memory_card_slot', models.CharField(max_length=256, null=True, verbose_name='Slot de Cartão de Memória')),
                ('memory_internal', models.CharField(max_length=256, null=True, verbose_name='Armazenamento Interno')),
                ('memory_other', models.CharField(max_length=256, null=True, verbose_name='Memória Outro(s)')),
                ('main_camera_type', models.CharField(max_length=256, null=True, verbose_name='Tipo de Câmera Principal')),
                ('main_camera_modules', models.TextField(max_length=512, null=True, verbose_name='Módulos da Câmera Principal')),
                ('main_camera_features', models.CharField(max_length=256, null=True, verbose_name='Recursos da Câmera Principal')),
                ('main_camera_video', models.CharField(max_length=256, null=True, verbose_name='Vídeo da Câmera Principal')),
                ('selfie_camera_type', models.CharField(max_length=256, null=True, verbose_name='Tipo de Câmera Selfie')),
                ('selfie_camera_modules', models.CharField(max_length=256, null=True, verbose_name='Módulos da Câmera Selfie')),
                ('selfie_camera_features', models.CharField(max_length=256, null=True, verbose_name='Recursos da Câmera Selfie')),
                ('selfie_camera_video', models.CharField(max_length=256, null=True, verbose_name='Vídeo da Câmera Selfie')),
                ('sound_loudspeaker', models.CharField(max_length=256, null=True, verbose_name='Alto-falante(s, null=True)')),
                ('sound_3_5mm_jack', models.CharField(max_length=256, null=True, verbose_name='Conector para Fone de Ouvido')),
                ('comms_wlan', models.CharField(max_length=256, null=True, verbose_name='WLAN')),
                ('comms_bluethoot', models.CharField(max_length=256, null=True, verbose_name='Bluetooth')),
                ('comms_gps', models.CharField(max_length=256, null=True, verbose_name='GPS')),
                ('comms_nfc', models.CharField(max_length=256, null=True, verbose_name='NFC')),
                ('comms_radio', models.CharField(max_length=256, null=True, verbose_name='Radio')),
                ('comms_usb', models.CharField(max_length=256, null=True, verbose_name='Entrada USB')),
                ('battery_type', models.CharField(max_length=256, null=True, verbose_name='Tipo de Bateria')),
                ('battery_charging', models.CharField(max_length=256, null=True, verbose_name='Carregamento de Bateria')),
                ('battery_standby', models.CharField(max_length=256, null=True, verbose_name='Bateria em Stand-by')),
                ('battery_music_play', models.CharField(max_length=256, null=True, verbose_name='Tempo de Reprodução de Música')),
                ('misc_colors', models.CharField(max_length=256, null=True, verbose_name='Cores')),
                ('misc_models', models.CharField(max_length=256, null=True, verbose_name='Modelos')),
                ('misc_sar_eu', models.CharField(max_length=256, null=True, verbose_name='SAR EU')),
                ('misc_price', models.CharField(max_length=256, null=True, verbose_name='Preços')),
                ('tests_performance', models.CharField(max_length=256, null=True, verbose_name='Testes de Performance')),
                ('tests_loudspeaker', models.CharField(max_length=256, null=True, verbose_name='Testes de Alto-falante(s, null=True)')),
                ('tests_battery_life', models.CharField(max_length=256, null=True, verbose_name='Testes de Vida de Bateria')),
                ('features_sensors', models.CharField(max_length=256, null=True, verbose_name='Sensores')),
                ('features_other', models.CharField(max_length=256, null=True, verbose_name='Recursos Outro(s)')),
                ('display_resolution_ppi', models.IntegerField(null=True, verbose_name='Resolução de Tela (dpi, null=True)')),
                ('display_size_inches', models.IntegerField(null=True, verbose_name='Tamanho de Tela (polegadas, null=True)')),
                ('display_size_screentobody_ratio', models.IntegerField(null=True, verbose_name='Relação Corpo Tela')),
                ('display_resolution_ppi_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Score Display Ppi')),
                ('display_size_inches_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Score Display Polegadas')),
                ('display_size_screentobody_ratio_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Score Display Relação')),
                ('main_camera_modules_mp', models.IntegerField(null=True, verbose_name='Resolução de Câmera Principal (MP)')),
                ('main_camera_modules_mp_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Score Câmera MP')),
                ('battery_type_mah', models.IntegerField(null=True, verbose_name='Capacidade de Bateria (mAh)')),
                ('battery_type_mah_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Score Battery MAh')),
                ('display_type_technology_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Score Display Tech')),
                ('display_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Display Score')),
                ('battery_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Battery Score')),
                ('camera_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Camera Score')),
                ('performance_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Performance Score')),
                ('vaibo_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Vaibo Score')),
                ('rank', models.IntegerField(null=True, verbose_name='Ranking')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
