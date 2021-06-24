from django.urls import path

from .views import IndexView, ProdutosList, ProdutoDescricao
# from .views import ProdutosList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar/produtos/', ProdutosList.as_view(), name='listar-produtos'),
    path('descricao/', ProdutoDescricao.as_view(), name='produto-descricao'),
]
