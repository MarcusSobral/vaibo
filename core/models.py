from django.db import models
# from django.db.models.fields import CharField

from stdimage.models import StdImageField


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
    batery_size = models.CharField('Capacidade da bateria', max_length=50)
    batery_size_unit = models.CharField('Capaciadade da bateria (unidade)', max_length=50)
    batery_type = models.CharField('Tipo de bateria', max_length=50)
    image = StdImageField('Imagem', upload_to='smartphone_img', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Smartphone'
        verbose_name_plural = 'Smartphones'

    def __str__(self):
        return self.name
