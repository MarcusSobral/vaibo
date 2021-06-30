from django.urls import path

from .views import IndexView, ProdutosList, ProdutoDescricao, ProdutosIndexView
from .views import UsuarioCreate
from .views import UsuarioUpdate
from .views import UsuarioDelete
# from .views import ProdutosList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('produtos/index/', ProdutosIndexView.as_view(), name='produtos-index'),
    path('produtos/lista/', ProdutosList.as_view(), name='produtos-lista'),
    path('produtos/descricao/<str:pk>', ProdutoDescricao.as_view(), name='produtos-descricao'),
    path('cadastrar/usuario/', UsuarioCreate.as_view(), name='cadastrar-usuario'),

    path('editar/usuario/<int:pk>', UsuarioUpdate.as_view(), name='editar-campo'),
    path('excluir/usuario/<int:pk>', UsuarioDelete.as_view(), name='excluir-campo'),
]
