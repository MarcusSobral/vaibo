from django.urls import path

from .views import IndexView, ProdutosList, ProdutoDescricao, ProdutosIndexView
# from .views import ProdutosList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('produtos/index/', ProdutosIndexView.as_view(), name='produtos-index'),
    path('produtos/lista/', ProdutosList.as_view(), name='produtos-lista'),
    path('produtos/descricao/', ProdutoDescricao.as_view(), name='produtos-descricao'),
]
