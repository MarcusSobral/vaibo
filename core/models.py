import uuid
from django.db import models
# from django.db.models.fields import CharField

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Smartphone(Base):
    name = models.CharField('Nome', max_length=100)
    maker = models.CharField('Fabricante', max_length=100)
    release_date = models.DateField('Data de lançamento', max_length=10)
    description = models.TextField('Descrição', max_length=200)
    body = models.CharField('Corpo', max_length=200)
    os = models.CharField('Sistema operacional', max_length=50)
    storage = models.CharField('Armazenamento', max_length=50)
    display_size_pixels = models.CharField('Tamanho da tela (pixels)', max_length=100)
    camera_pixels = models.CharField('Resolução da Câmera', max_length=50)
    camera_pixels_unit = models.CharField('Resolução da Câmera (unidade)', max_length=50)
    ram_size = models.CharField('Memória RAM', max_length=50)
    ram_size_unit = models.CharField('Memória RAM (unidade)', max_length=50)
    chipset_short = models.CharField('Processador', max_length=50)
    battery_size = models.CharField('Capacidade da bateria', max_length=50)
    battery_size_unit = models.CharField('Capaciadade da bateria (unidade)', max_length=50)
    battery_type = models.CharField('Tipo de bateria', max_length=50)
    image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Smartphone'
        verbose_name_plural = 'Smartphones'

    def __str__(self):
        return self.name


class Produtos(Base):
    identification_id = models.CharField('ID', max_length=50)
    identification_title = models.CharField('Título', max_length=60)
    identification_name_maker = models.CharField('Fabricante', max_length=30)
    identification_name = models.CharField('Nome', max_length=40)
    identification_versions = models.CharField('Versões', max_length=250)
    identification_announced = models.CharField('Anunciado', max_length=30)
    identification_released = models.CharField('Lançado', max_length=30)
    identification_status = models.CharField('Status', max_length=40)
    network_technology = models.CharField('Tecnologia', max_length=40)
    network_bands_2g = models.CharField('Bandas 2G', max_length=70)
    network_bands_3g = models.CharField('Bandas 3G', max_length=70)
    network_bands_4g = models.CharField('Bandas 4G', max_length=120)
    network_bands_5g = models.CharField('Bandas 5G', max_length=100)
    body_dimensions = models.CharField('Dimenções', max_length=70)
    body_weight = models.CharField('Peso', max_length=50)
    body_build = models.CharField('Construção', max_length=50)
    body_sim = models.CharField('SIM', max_length=200)
    body_other = models.CharField('Corpo Outro(s)', max_length=200)
    display_type = models.CharField('Tipo de Tela', max_length=100)
    display_size = models.CharField('Tamanho da Tela', max_length=60)
    display_resolution = models.CharField('Resolução da Tela', max_length=60)
    display_protection = models.CharField('Proteção da Tela', max_length=150)
    display_type.technology = models.CharField('Tecnologia da Tela', max_length=50)
    display_other = models.CharField('Tela Outro(s)', max_length=100)
    platform_os = models.CharField('Sistema Operacional', max_length=100)
    platform_chipset = models.CharField('Processador', max_length=200)
    platform_cpu = models.CharField('CPU', max_length=200)
    platform_gpu = models.CharField('GPU', max_length=100)
    memory_card_slot = models.CharField('Slot de Cartão de Memória', max_length=100)
    memory_internal = models.CharField('Armazenamento Interno', max_length=150)
    memory_other = models.CharField('Memória Outro(s)', max_length=100)
    main_camera_type = models.CharField('Tipo de Câmera Principal', max_length=50)
    main_camera_modules = models.CharField('Módulos da Câmera Principal', max_length=350)
    main_camera_features = models.CharField('Recursos da Câmera Principal', max_length=100)
    main_camera_video = models.CharField('Vídeo da Câmera Principal', max_length=150)
    selfie_camera_type = models.CharField('Tipo de Câmera Selfie', max_length=20)
    selfie_camera_modules = models.CharField('Módulos da Câmera Selfie', max_length=100)
    selfie_camera_features = models.CharField('Recursos da Câmera Selfie', max_length=100)
    selfie_camera_video = models.CharField('Vídeo da Câmera Selfie', max_length=100)
    sound_loudspeaker = models.CharField('Alto-falante(s)', max_length=100)
    sound_35mm_jack = models.CharField('Conector para Fone de Ouvido', max_length=100)
    comms_wlan = models.CharField('WLAN', max_length=100)
    comms_bluethoot = models.CharField('Bluetooth', max_length=100)
    comms_gps = models.CharField('GPS', max_length=100)
    comms_nfc = models.CharField('NFC', max_length=100)
    comms_radio = models.CharField('Radio', max_length=100)
    comms_usb = models.CharField('Entrada USB', max_length=100)
    battery_type = models.CharField('Tipo de Bateria', max_length=100)
    battery_charging = models.CharField('Carregamento de Bateria', max_length=100)
    battery_standby = models.CharField('Bateria em Stand-by', max_length=100)
    battery_music_play = models.CharField('Tempo de Reprodução de Música', max_length=100)
    misc_colors = models.CharField('Cores', max_length=100)
    misc_models = models.CharField('Modelos', max_length=100)
    misc_sar_eu = models.CharField('SAR EU', max_length=100)
    misc_price = models.CharField('Preços', max_length=100)
    tests_performance = models.CharField('Testes de Performance', max_length=100)
    tests_loudspeaker = models.CharField('Testes de Alto-falante(s)', max_length=100)
    tests_battery_life = models.CharField('Testes de Vida de Bateria', max_length=100)
    features_sensors = models.CharField('Sensores', max_length=100)
    features_other = models.CharField('Recursos Outro(s)', max_length=100)
    display_resolution.ppi = models.IntegerField('Resolução de Tela (dpi)')
    display_size.inches = models.IntegerField('Tamanho de Tela (polegadas)')
    display_size_screentobody_ratio = models.IntegerField('Relação Corpo Tela')
    display_resolution.ppi_score = models.DecimalField('Score Display Ppi', decimal_places=1, max_digits=2)
    display_size.inches_score = models.DecimalField('Score Display Polegadas', decimal_places=1, max_digits=2)
    display_size_screentobody_ratio_score = models.DecimalField('Score Display Relação', decimal_places=1, max_digits=2)
    main_camera_modules_mp = models.IntegerField('Resolução de Câmera Principal (MP)')
    main_camera_modules_mp_score = models.DecimalField('Score Câmera MP', decimal_places=1, max_digits=2)
    battery_type_mah = models.IntegerField('Capacidade de Bateria (mAh)')
    battery_type_mah_score = models.DecimalField('Score Battery MAh', decimal_places=1, max_digits=2)
    display_type_technology_score = models.DecimalField('Score Display Tech', decimal_places=1, max_digits=2)
    display_score = models.DecimalField('Display Score', decimal_places=1, max_digits=2)
    battery_score = models.DecimalField('Battery Score', decimal_places=1, max_digits=2)
    camera_score = models.DecimalField('Camera Score', decimal_places=1, max_digits=2)
    performance_score = models.DecimalField('Performance Score', decimal_places=1, max_digits=2)
    vaibo_score = models.DecimalField('Vaibo Score', decimal_places=1, max_digits=2)
    rank = models.IntegerField('Ranking')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name
