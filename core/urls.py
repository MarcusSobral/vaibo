from django.urls import path

from .views import IndexView
from .views import ProdutosList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar/produtos/', ProdutosList.as_view(), name='listar-produtos'),
]
