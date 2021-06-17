import uuid
from django.db import models
from django.db.models.fields import DateField
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
    name = models.CharField('Nome', max_length=255)
    maker = models.CharField('Fabricante', max_length=255)
    release_date = models.DateField('Data de lançamento', max_length=10)
    description = models.TextField('Descrição', max_length=255, null=True)
    body = models.CharField('Corpo', max_length=255, null=True)
    os = models.CharField('Sistema operacional', max_length=255, null=True)
    storage = models.CharField('Armazenamento', max_length=255, null=True)
    display_size_pixels = models.CharField('Tamanho da tela (pixels, null=True)', max_length=255, null=True)
    camera_pixels = models.CharField('Resolução da Câmera', max_length=255, null=True)
    camera_pixels_unit = models.CharField('Resolução da Câmera (unidade, null=True)', max_length=255, null=True)
    ram_size = models.CharField('Memória RAM', max_length=255, null=True)
    ram_size_unit = models.CharField('Memória RAM (unidade, null=True)', max_length=255, null=True)
    chipset_short = models.CharField('Processador', max_length=255, null=True)
    battery_size = models.CharField('Capacidade da bateria', max_length=255, null=True)
    battery_size_unit = models.CharField('Capaciadade da bateria (unidade, null=True)', max_length=255, null=True)
    battery_type = models.CharField('Tipo de bateria', max_length=255, null=True)
    image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Smartphone'
        verbose_name_plural = 'Smartphones'

    def __str__(self):
        return self.name


class Produtos(Base):
    id = models.CharField(primary_key=True, default=uuid.uuid4(), unique=True, max_length=255)
    identification_id = models.CharField('ID', max_length=255)
    identification_title = models.CharField('Título', max_length=255, null=True)
    identification_name_maker = models.CharField('Fabricante', max_length=255)
    identification_name = models.CharField('Nome', max_length=255)
    identification_versions = models.CharField('Versões', max_length=255, null=True)
    identification_announced = models.CharField('Anunciado', max_length=255, null=True)
    identification_announced_date = DateField("Data de Anúncio", max_length=10, null=True)
    identification_released = models.CharField('Lançado', max_length=255, null=True)
    identification_released_date = models.DateField("Data de Lançamento", max_length=10, null=True)
    identification_status = models.CharField('Status', max_length=255, null=True)
    network_technology = models.CharField('Tecnologia', max_length=255, null=True)
    network_bands_2g = models.CharField('Bandas 2G', max_length=255, null=True)
    network_bands_3g = models.CharField('Bandas 3G', max_length=255, null=True)
    network_bands_4g = models.CharField('Bandas 4G', max_length=255, null=True)
    network_bands_5g = models.CharField('Bandas 5G', max_length=255, null=True)
    body_dimensions = models.CharField('Dimenções', max_length=255, null=True)
    body_weight = models.CharField('Peso', max_length=255, null=True)
    body_build = models.CharField('Construção', max_length=255, null=True)
    body_sim = models.CharField('SIM', max_length=255, null=True)
    body_other = models.CharField('Corpo Outro(s)', max_length=255, null=True)
    display_type = models.CharField('Tipo de Tela', max_length=255, null=True)
    display_size = models.CharField('Tamanho da Tela', max_length=255, null=True)
    display_resolution = models.CharField('Resolução da Tela', max_length=255, null=True)
    display_protection = models.CharField('Proteção da Tela', max_length=255, null=True)
    display_type_technology = models.CharField('Tecnologia da Tela', max_length=255, null=True)
    display_other = models.CharField('Tela Outro(s)', max_length=255, null=True)
    platform_os = models.CharField('Sistema Operacional', max_length=255, null=True)
    platform_chipset = models.CharField('Processador', max_length=255, null=True)
    platform_cpu = models.CharField('CPU', max_length=255, null=True)
    platform_gpu = models.CharField('GPU', max_length=255, null=True)
    memory_card_slot = models.CharField('Slot de Cartão de Memória', max_length=255, null=True)
    memory_internal = models.CharField('Armazenamento Interno', max_length=255, null=True)
    memory_other = models.CharField('Memória Outro(s)', max_length=255, null=True)
    main_camera_type = models.CharField('Tipo de Câmera Principal', max_length=255, null=True)
    main_camera_modules = models.TextField('Módulos da Câmera Principal', max_length=512, null=True)
    main_camera_features = models.CharField('Recursos da Câmera Principal', max_length=255, null=True)
    main_camera_video = models.CharField('Vídeo da Câmera Principal', max_length=255, null=True)
    selfie_camera_type = models.CharField('Tipo de Câmera Selfie', max_length=255, null=True)
    selfie_camera_modules = models.CharField('Módulos da Câmera Selfie', max_length=255, null=True)
    selfie_camera_features = models.CharField('Recursos da Câmera Selfie', max_length=255, null=True)
    selfie_camera_video = models.CharField('Vídeo da Câmera Selfie', max_length=255, null=True)
    sound_loudspeaker = models.CharField('Alto-falante(s, null=True)', max_length=255, null=True)
    sound_3_5mm_jack = models.CharField('Conector para Fone de Ouvido', max_length=255, null=True)
    comms_wlan = models.CharField('WLAN', max_length=255, null=True)
    comms_bluethoot = models.CharField('Bluetooth', max_length=255, null=True)
    comms_gps = models.CharField('GPS', max_length=255, null=True)
    comms_nfc = models.CharField('NFC', max_length=255, null=True)
    comms_radio = models.CharField('Radio', max_length=255, null=True)
    comms_usb = models.CharField('Entrada USB', max_length=255, null=True)
    battery_type = models.CharField('Tipo de Bateria', max_length=255, null=True)
    battery_charging = models.CharField('Carregamento de Bateria', max_length=255, null=True)
    battery_standby = models.CharField('Bateria em Stand-by', max_length=255, null=True)
    battery_music_play = models.CharField('Tempo de Reprodução de Música', max_length=255, null=True)
    misc_colors = models.CharField('Cores', max_length=255, null=True)
    misc_models = models.CharField('Modelos', max_length=255, null=True)
    misc_sar_eu = models.CharField('SAR EU', max_length=255, null=True)
    misc_price = models.CharField('Preços', max_length=255, null=True)
    tests_performance = models.CharField('Testes de Performance', max_length=255, null=True)
    tests_loudspeaker = models.CharField('Testes de Alto-falante(s, null=True)', max_length=255, null=True)
    tests_battery_life = models.CharField('Testes de Vida de Bateria', max_length=255, null=True)
    features_sensors = models.CharField('Sensores', max_length=255, null=True)
    features_other = models.CharField('Recursos Outro(s)', max_length=255, null=True)
    display_resolution_ppi = models.IntegerField('Resolução de Tela (dpi, null=True)', null=True)
    display_size_inches = models.IntegerField('Tamanho de Tela (polegadas, null=True)', null=True)
    display_size_screentobody_ratio = models.IntegerField('Relação Corpo Tela', null=True)
    display_resolution_ppi_score = models.DecimalField('Score Display Ppi', decimal_places=1, max_digits=2, null=True)
    display_size_inches_score = models.DecimalField('Score Display Polegadas', decimal_places=1, max_digits=2, null=True)
    display_size_screentobody_ratio_score = models.DecimalField('Score Display Relação', decimal_places=1, max_digits=2, null=True)
    main_camera_modules_mp = models.IntegerField('Resolução de Câmera Principal (MP)', null=True)
    main_camera_modules_mp_score = models.DecimalField('Score Câmera MP', decimal_places=1, max_digits=2, null=True)
    battery_type_mah = models.IntegerField('Capacidade de Bateria (mAh)', null=True)
    battery_type_mah_score = models.DecimalField('Score Battery MAh', decimal_places=1, max_digits=2, null=True)
    display_type_technology_score = models.DecimalField('Score Display Tech', decimal_places=1, max_digits=2, null=True)
    display_score = models.CharField('Display_score', max_length=10, null=True)
    battery_score = models.CharField('Battery_score', max_length=10, null=True)
    camera_score = models.CharField('Camera_score', max_length=10, null=True)
    performance_score = models.CharField('Performance_score', max_length=10, null=True)
    client_score = models.CharField('Cliente_score', max_length=10, null=True)
    expert_score = models.CharField('Expert_score', max_length=10, null=True)
    vaibo_score = models.DecimalField('Vaibo Score', decimal_places=1, max_digits=2, null=True)
    rank = models.IntegerField('Ranking', null=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self, null=True):
        return self.name
